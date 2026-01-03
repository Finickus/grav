# PowerShell script to find duplicate pages in Grav CMS

$pagesDir = Join-Path $PSScriptRoot "user\pages"

Write-Host "Scanning pages for duplicates..." -ForegroundColor Cyan

# Find all markdown files
$allPages = Get-ChildItem -Path $pagesDir -Recurse -Filter "*.md"
Write-Host "Found $($allPages.Count) total pages`n" -ForegroundColor Green

# Group files by content hash
$hashTable = @{}

foreach ($page in $allPages) {
    try {
        $hash = (Get-FileHash -Path $page.FullName -Algorithm MD5).Hash
        
        if ($hashTable.ContainsKey($hash)) {
            $hashTable[$hash] += @($page.FullName)
        }
        else {
            $hashTable[$hash] = @($page.FullName)
        }
    }
    catch {
        Write-Host "Error reading $($page.FullName): $_" -ForegroundColor Red
    }
}

# Find duplicates
$duplicates = $hashTable.GetEnumerator() | Where-Object { $_.Value.Count -gt 1 }

Write-Host "Found $($duplicates.Count) groups of duplicates" -ForegroundColor Yellow
Write-Host ("=" * 80)

$blogFilesToDelete = @()

foreach ($group in $duplicates) {
    Write-Host "`nDuplicate group ($($group.Value.Count) files):" -ForegroundColor Yellow
    
    $blogFiles = @()
    $otherFiles = @()
    
    foreach ($file in $group.Value) {
        $relPath = $file.Replace($pagesDir, "").TrimStart("\")
        
        if ($file -like "*\07.blog\*") {
            $blogFiles += $file
            Write-Host "  [BLOG] $relPath" -ForegroundColor Red
        }
        else {
            $otherFiles += $file
            Write-Host "  [OTHER] $relPath" -ForegroundColor Green
        }
    }
    
    # If there are duplicates with at least one in blog and one outside blog
    if ($blogFiles.Count -gt 0 -and $otherFiles.Count -gt 0) {
        $blogFilesToDelete += $blogFiles
        Write-Host "  → Will delete $($blogFiles.Count) blog file(s)" -ForegroundColor Magenta
    }
}

Write-Host "`n$("=" * 80)" -ForegroundColor Cyan
Write-Host "DRY RUN - Files that would be deleted:" -ForegroundColor Cyan
Write-Host ("=" * 80)

foreach ($file in $blogFilesToDelete) {
    Write-Host "  - $file" -ForegroundColor Red
}

Write-Host "`nTotal: $($blogFilesToDelete.Count) files would be deleted" -ForegroundColor Yellow

# Save list to file for review
$blogFilesToDelete | Out-File -FilePath "files_to_delete.txt" -Encoding UTF8
Write-Host "`nList saved to files_to_delete.txt" -ForegroundColor Green

# Uncomment the following lines to actually delete the files
# Write-Host "`n`nDo you want to delete these files? (y/n): " -NoNewline -ForegroundColor Yellow
# $confirm = Read-Host
# if ($confirm -eq 'y' -or $confirm -eq 'Y') {
#     foreach ($file in $blogFilesToDelete) {
#         try {
#             Remove-Item -Path $file -Force
#             Write-Host "  ✓ Deleted: $file" -ForegroundColor Green
#         } catch {
#             Write-Host "  ✗ Error deleting $file: $_" -ForegroundColor Red
#         }
#     }
#     Write-Host "`nDeletion complete!" -ForegroundColor Green
# } else {
#     Write-Host "`nDeletion cancelled." -ForegroundColor Yellow
# }
