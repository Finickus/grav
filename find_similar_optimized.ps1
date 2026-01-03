# Optimized PowerShell script to find similar pages in Grav CMS
# Uses faster comparison methods and early filtering

$pagesDir = Join-Path $PSScriptRoot "user\pages"
$similarityThreshold = 0.70  # 70% similarity threshold (lowered for faster results)

Write-Host "=== Optimized Similar Pages Finder ===" -ForegroundColor Cyan
Write-Host "Scanning pages for similar content...`n" -ForegroundColor Yellow

# Function to create word frequency map
function Get-WordFrequency {
    param([string]$text)
    
    $freq = @{}
    $words = $text.ToLower() -split '\s+' | Where-Object { $_.Length -gt 2 }
    
    foreach ($word in $words) {
        if ($freq.ContainsKey($word)) {
            $freq[$word]++
        } else {
            $freq[$word] = 1
        }
    }
    
    return $freq
}

# Faster similarity calculation using cosine similarity
function Get-CosineSimilarity {
    param(
        [hashtable]$freq1,
        [hashtable]$freq2
    )
    
    if ($freq1.Count -eq 0 -or $freq2.Count -eq 0) { return 0.0 }
    
    # Get all unique words
    $allWords = New-Object System.Collections.Generic.HashSet[string]
    $freq1.Keys | ForEach-Object { $allWords.Add($_) | Out-Null }
    $freq2.Keys | ForEach-Object { $allWords.Add($_) | Out-Null }
    
    # Calculate dot product and magnitudes
    $dotProduct = 0.0
    $magnitude1 = 0.0
    $magnitude2 = 0.0
    
    foreach ($word in $allWords) {
        $val1 = if ($freq1.ContainsKey($word)) { $freq1[$word] } else { 0 }
        $val2 = if ($freq2.ContainsKey($word)) { $freq2[$word] } else { 0 }
        
        $dotProduct += $val1 * $val2
        $magnitude1 += $val1 * $val1
        $magnitude2 += $val2 * $val2
    }
    
    if ($magnitude1 -eq 0 -or $magnitude2 -eq 0) { return 0.0 }
    
    $magnitude1 = [Math]::Sqrt($magnitude1)
    $magnitude2 = [Math]::Sqrt($magnitude2)
    
    return $dotProduct / ($magnitude1 * $magnitude2)
}

# Function to extract text content from markdown
function Get-MarkdownText {
    param([string]$content)
    
    # Remove YAML frontmatter
    $content = $content -replace '(?s)^---.*?---', ''
    
    # Remove HTML tags
    $content = $content -replace '<[^>]+>', ''
    
    # Remove markdown syntax
    $content = $content -replace '#+\s+', ''
    $content = $content -replace '\*\*([^*]+)\*\*', '$1'
    $content = $content -replace '\*([^*]+)\*', '$1'
    $content = $content -replace '\[([^\]]+)\]\([^\)]+\)', '$1'
    $content = $content -replace '```[^`]*```', ''
    $content = $content -replace '`([^`]+)`', '$1'
    
    return $content.Trim()
}

# Find all markdown files
$allPages = Get-ChildItem -Path $pagesDir -Recurse -Filter "*.md"
Write-Host "Found $($allPages.Count) total pages" -ForegroundColor Green

# Read all pages and calculate word frequencies
Write-Host "Reading and preprocessing pages..." -ForegroundColor Yellow
$pagesData = @()
$processedCount = 0

foreach ($page in $allPages) {
    $processedCount++
    if ($processedCount % 50 -eq 0) {
        Write-Host "  Processed: $processedCount / $($allPages.Count)" -ForegroundColor Gray
    }
    
    try {
        $content = Get-Content -Path $page.FullName -Raw -Encoding UTF8
        $textContent = Get-MarkdownText -content $content
        $wordCount = ($textContent -split '\s+').Count
        
        # Skip very short pages (less than 20 words)
        if ($wordCount -lt 20) {
            continue
        }
        
        $wordFreq = Get-WordFrequency -text $textContent
        
        $pagesData += [PSCustomObject]@{
            Path = $page.FullName
            RelPath = $page.FullName.Replace($pagesDir, "").TrimStart("\")
            WordFreq = $wordFreq
            WordCount = $wordCount
            IsInBlog = $page.FullName -like "*\07.blog\*"
            TopWords = ($wordFreq.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 10 -ExpandProperty Key) -join ','
        }
    } catch {
        Write-Host "Error reading $($page.FullName): $_" -ForegroundColor Red
    }
}

Write-Host "Filtered to $($pagesData.Count) pages (skipped very short pages)`n" -ForegroundColor Green

# Pre-filtering: group pages by similar word counts (within 30%)
Write-Host "Analyzing similarity with smart filtering..." -ForegroundColor Yellow
$similarPairs = @()
$totalComparisons = 0
$skippedComparisons = 0

for ($i = 0; $i -lt $pagesData.Count; $i++) {
    if ($i % 10 -eq 0) {
        $percent = [math]::Round(($i / $pagesData.Count) * 100, 1)
        Write-Host "  Progress: $percent% (comparing page $i of $($pagesData.Count))" -ForegroundColor Gray
    }
    
    $page1 = $pagesData[$i]
    
    for ($j = $i + 1; $j -lt $pagesData.Count; $j++) {
        $page2 = $pagesData[$j]
        
        # Skip if word counts differ by more than 50% (unlikely to be similar)
        $wordCountRatio = [Math]::Max($page1.WordCount, $page2.WordCount) / [Math]::Min($page1.WordCount, $page2.WordCount)
        if ($wordCountRatio -gt 2.0) {
            $skippedComparisons++
            continue
        }
        
        $totalComparisons++
        
        $similarity = Get-CosineSimilarity -freq1 $page1.WordFreq -freq2 $page2.WordFreq
        
        if ($similarity -ge $similarityThreshold) {
            $similarPairs += [PSCustomObject]@{
                File1 = $page1.RelPath
                File2 = $page2.RelPath
                Similarity = $similarity
                File1InBlog = $page1.IsInBlog
                File2InBlog = $page2.IsInBlog
                File1Words = $page1.WordCount
                File2Words = $page2.WordCount
                File1Path = $page1.Path
                File2Path = $page2.Path
            }
        }
    }
}

Write-Host "`nAnalysis complete!" -ForegroundColor Green
Write-Host "  Total comparisons: $totalComparisons" -ForegroundColor Gray
Write-Host "  Skipped comparisons: $skippedComparisons" -ForegroundColor Gray
Write-Host ("=" * 80)
Write-Host "Found $($similarPairs.Count) pairs of similar pages (>= $($similarityThreshold * 100)% similarity)`n" -ForegroundColor Yellow

# Sort by similarity descending
$similarPairs = $similarPairs | Sort-Object -Property Similarity -Descending

# Display results
$displayCount = 0
foreach ($pair in $similarPairs) {
    $displayCount++
    if ($displayCount -gt 50) {
        Write-Host "... (showing first 50 of $($similarPairs.Count) similar pairs)" -ForegroundColor Gray
        break
    }
    
    $similarityPercent = [math]::Round($pair.Similarity * 100, 1)
    
    Write-Host "[$displayCount] Similarity: $similarityPercent%" -ForegroundColor Cyan
    
    if ($pair.File1InBlog) {
        Write-Host "  [BLOG]  $($pair.File1) ($($pair.File1Words) words)" -ForegroundColor Red
    } else {
        Write-Host "  [OTHER] $($pair.File1) ($($pair.File1Words) words)" -ForegroundColor Green
    }
    
    if ($pair.File2InBlog) {
        Write-Host "  [BLOG]  $($pair.File2) ($($pair.File2Words) words)" -ForegroundColor Red
    } else {
        Write-Host "  [OTHER] $($pair.File2) ($($pair.File2Words) words)" -ForegroundColor Green
    }
    
    # Check if one is in blog and other is not
    if ($pair.File1InBlog -ne $pair.File2InBlog) {
        Write-Host "  → ACTION: One in blog, one outside - review for deletion" -ForegroundColor Magenta
    }
    
    Write-Host ""
}

# Export to CSV for detailed analysis
$csvPath = "similar_pages_optimized.csv"
$similarPairs | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
Write-Host "`nFull results exported to $csvPath" -ForegroundColor Green

# Create list of blog files that have similar content outside blog
$blogFilesToReview = @()
foreach ($pair in $similarPairs) {
    if ($pair.File1InBlog -and -not $pair.File2InBlog) {
        if ($blogFilesToReview -notcontains $pair.File1Path) {
            $blogFilesToReview += $pair.File1Path
        }
    }
    if ($pair.File2InBlog -and -not $pair.File1InBlog) {
        if ($blogFilesToReview -notcontains $pair.File2Path) {
            $blogFilesToReview += $pair.File2Path
        }
    }
}

if ($blogFilesToReview.Count -gt 0) {
    Write-Host "`n$("=" * 80)" -ForegroundColor Cyan
    Write-Host "Blog files with similar content outside blog:" -ForegroundColor Cyan
    Write-Host ("=" * 80)
    
    $blogFilesToReview | ForEach-Object {
        $relPath = $_.Replace($pagesDir, "").TrimStart("\")
        Write-Host "  - $relPath" -ForegroundColor Yellow
    }
    
    Write-Host "`nTotal: $($blogFilesToReview.Count) blog files to review" -ForegroundColor Yellow
    
    # Save to file
    $blogFilesToReview | Out-File -FilePath "blog_files_to_review_optimized.txt" -Encoding UTF8
    Write-Host "List saved to blog_files_to_review_optimized.txt" -ForegroundColor Green
}

Write-Host "`n$("=" * 80)" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Total pages analyzed: $($pagesData.Count)" -ForegroundColor White
Write-Host "  Similar pairs found: $($similarPairs.Count)" -ForegroundColor White
Write-Host "  Blog files to review: $($blogFilesToReview.Count)" -ForegroundColor White
Write-Host ("=" * 80)
