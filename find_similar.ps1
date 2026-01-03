# PowerShell script to find similar pages in Grav CMS
# Uses text comparison to find pages with high similarity

$pagesDir = Join-Path $PSScriptRoot "user\pages"
$similarityThreshold = 0.80  # 80% similarity threshold

Write-Host "Scanning pages for similar content..." -ForegroundColor Cyan

# Function to calculate Jaccard similarity between two strings
function Get-JaccardSimilarity {
    param(
        [string]$text1,
        [string]$text2
    )
    
    # Split into words and create sets
    $words1 = $text1.ToLower() -split '\s+' | Where-Object { $_.Length -gt 2 }
    $words2 = $text2.ToLower() -split '\s+' | Where-Object { $_.Length -gt 2 }
    
    if ($words1.Count -eq 0 -and $words2.Count -eq 0) { return 1.0 }
    if ($words1.Count -eq 0 -or $words2.Count -eq 0) { return 0.0 }
    
    $set1 = New-Object System.Collections.Generic.HashSet[string]
    $set2 = New-Object System.Collections.Generic.HashSet[string]
    
    $words1 | ForEach-Object { $set1.Add($_) | Out-Null }
    $words2 | ForEach-Object { $set2.Add($_) | Out-Null }
    
    # Calculate intersection
    $intersection = New-Object System.Collections.Generic.HashSet[string]($set1)
    $intersection.IntersectWith($set2)
    
    # Calculate union
    $union = New-Object System.Collections.Generic.HashSet[string]($set1)
    $union.UnionWith($set2)
    
    if ($union.Count -eq 0) { return 0.0 }
    
    return [double]$intersection.Count / [double]$union.Count
}

# Function to extract text content from markdown
function Get-MarkdownText {
    param([string]$content)
    
    # Remove YAML frontmatter
    $content = $content -replace '(?s)^---.*?---', ''
    
    # Remove HTML tags
    $content = $content -replace '<[^>]+>', ''
    
    # Remove markdown syntax
    $content = $content -replace '#+\s+', ''  # Headers
    $content = $content -replace '\*\*([^*]+)\*\*', '$1'  # Bold
    $content = $content -replace '\*([^*]+)\*', '$1'  # Italic
    $content = $content -replace '\[([^\]]+)\]\([^\)]+\)', '$1'  # Links
    $content = $content -replace '```[^`]*```', ''  # Code blocks
    $content = $content -replace '`([^`]+)`', '$1'  # Inline code
    
    return $content.Trim()
}

# Find all markdown files
$allPages = Get-ChildItem -Path $pagesDir -Recurse -Filter "*.md"
Write-Host "Found $($allPages.Count) total pages`n" -ForegroundColor Green

# Read all pages and their content
Write-Host "Reading page contents..." -ForegroundColor Yellow
$pagesData = @()

foreach ($page in $allPages) {
    try {
        $content = Get-Content -Path $page.FullName -Raw -Encoding UTF8
        $textContent = Get-MarkdownText -content $content
        
        $pagesData += [PSCustomObject]@{
            Path        = $page.FullName
            RelPath     = $page.FullName.Replace($pagesDir, "").TrimStart("\")
            TextContent = $textContent
            WordCount   = ($textContent -split '\s+').Count
            IsInBlog    = $page.FullName -like "*\07.blog\*"
        }
    }
    catch {
        Write-Host "Error reading $($page.FullName): $_" -ForegroundColor Red
    }
}

Write-Host "Analyzing similarity..." -ForegroundColor Yellow
$similarPairs = @()
$totalComparisons = ($pagesData.Count * ($pagesData.Count - 1)) / 2
$currentComparison = 0

# Compare all pairs
for ($i = 0; $i -lt $pagesData.Count; $i++) {
    for ($j = $i + 1; $j -lt $pagesData.Count; $j++) {
        $currentComparison++
        
        # Progress indicator every 1000 comparisons
        if ($currentComparison % 1000 -eq 0) {
            $percent = [math]::Round(($currentComparison / $totalComparisons) * 100, 1)
            Write-Host "  Progress: $percent% ($currentComparison / $totalComparisons)" -ForegroundColor Gray
        }
        
        $page1 = $pagesData[$i]
        $page2 = $pagesData[$j]
        
        # Skip if both pages are very short
        if ($page1.WordCount -lt 10 -or $page2.WordCount -lt 10) {
            continue
        }
        
        $similarity = Get-JaccardSimilarity -text1 $page1.TextContent -text2 $page2.TextContent
        
        if ($similarity -ge $similarityThreshold) {
            $similarPairs += [PSCustomObject]@{
                File1       = $page1.RelPath
                File2       = $page2.RelPath
                Similarity  = $similarity
                File1InBlog = $page1.IsInBlog
                File2InBlog = $page2.IsInBlog
                File1Words  = $page1.WordCount
                File2Words  = $page2.WordCount
            }
        }
    }
}

Write-Host "`nAnalysis complete!" -ForegroundColor Green
Write-Host ("=" * 80)
Write-Host "Found $($similarPairs.Count) pairs of similar pages (>= $($similarityThreshold * 100)% similarity)`n" -ForegroundColor Yellow

# Sort by similarity descending
$similarPairs = $similarPairs | Sort-Object -Property Similarity -Descending

# Display results
foreach ($pair in $similarPairs) {
    $similarityPercent = [math]::Round($pair.Similarity * 100, 1)
    
    Write-Host "Similarity: $similarityPercent%" -ForegroundColor Cyan
    
    if ($pair.File1InBlog) {
        Write-Host "  [BLOG]  $($pair.File1) ($($pair.File1Words) words)" -ForegroundColor Red
    }
    else {
        Write-Host "  [OTHER] $($pair.File1) ($($pair.File1Words) words)" -ForegroundColor Green
    }
    
    if ($pair.File2InBlog) {
        Write-Host "  [BLOG]  $($pair.File2) ($($pair.File2Words) words)" -ForegroundColor Red
    }
    else {
        Write-Host "  [OTHER] $($pair.File2) ($($pair.File2Words) words)" -ForegroundColor Green
    }
    
    # Check if one is in blog and other is not
    if ($pair.File1InBlog -ne $pair.File2InBlog) {
        Write-Host "  → ACTION: Consider deleting blog version" -ForegroundColor Magenta
    }
    
    Write-Host ""
}

# Export to CSV for detailed analysis
$csvPath = "similar_pages.csv"
$similarPairs | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
Write-Host "Results exported to $csvPath" -ForegroundColor Green

# Create list of blog files to potentially delete
$blogFilesToReview = @()
foreach ($pair in $similarPairs) {
    if ($pair.File1InBlog -and -not $pair.File2InBlog) {
        $blogFilesToReview += Join-Path $pagesDir $pair.File1
    }
    if ($pair.File2InBlog -and -not $pair.File1InBlog) {
        $blogFilesToReview += Join-Path $pagesDir $pair.File2
    }
}

if ($blogFilesToReview.Count -gt 0) {
    Write-Host "`n$("=" * 80)" -ForegroundColor Cyan
    Write-Host "Blog files to review for deletion (have similar content outside blog):" -ForegroundColor Cyan
    Write-Host ("=" * 80)
    
    $blogFilesToReview | ForEach-Object {
        Write-Host "  - $_" -ForegroundColor Yellow
    }
    
    Write-Host "`nTotal: $($blogFilesToReview.Count) blog files to review" -ForegroundColor Yellow
    
    # Save to file
    $blogFilesToReview | Out-File -FilePath "blog_files_to_review.txt" -Encoding UTF8
    Write-Host "List saved to blog_files_to_review.txt" -ForegroundColor Green
}

Write-Host "`n$("=" * 80)" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Total pages analyzed: $($pagesData.Count)" -ForegroundColor White
Write-Host "  Similar pairs found: $($similarPairs.Count)" -ForegroundColor White
Write-Host "  Blog files to review: $($blogFilesToReview.Count)" -ForegroundColor White
Write-Host ("=" * 80)
