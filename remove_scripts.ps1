# Script to remove jQuery and Bootstrap JS from markdown files

$PAGES_DIR = "c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"

$stats = @{
    files_processed        = 0
    files_modified         = 0
    jquery_removed         = 0
    bootstrap_removed      = 0
    popper_removed         = 0
    comments_removed       = 0
    jquery_scripts_removed = 0
}

function Remove-ScriptsFromFile {
    param([string]$FilePath)
    
    $content = Get-Content -Path $FilePath -Raw -Encoding UTF8
    $originalContent = $content
    $script:stats.files_processed++
    
    $modified = $false
    
    $jqueryPattern = '<script\s+src=["' + "'" + ']https?://code\.jquery\.com/jquery-[^"' + "'" + ']+["' + "'" + ']>\s*</script>'
    if ($content -match $jqueryPattern) {
        $matches = [regex]::Matches($content, $jqueryPattern)
        $script:stats.jquery_removed += $matches.Count
        $content = $content -replace $jqueryPattern, ''
        $modified = $true
    }
    
    $bootstrapPattern = '<script\s+src=["' + "'" + ']https?://(cdn\.jsdelivr\.net/npm/bootstrap|stackpath\.bootstrapcdn\.com/bootstrap)/[^"' + "'" + ']+["' + "'" + ']>\s*</script>'
    if ($content -match $bootstrapPattern) {
        $matches = [regex]::Matches($content, $bootstrapPattern)
        $script:stats.bootstrap_removed += $matches.Count
        $content = $content -replace $bootstrapPattern, ''
        $modified = $true
    }
    
    $popperPattern = '<script\s+src=["' + "'" + ']https?://cdn\.jsdelivr\.net/npm/popper\.js@[^"' + "'" + ']+["' + "'" + ']>\s*</script>'
    if ($content -match $popperPattern) {
        $matches = [regex]::Matches($content, $popperPattern)
        $script:stats.popper_removed += $matches.Count
        $content = $content -replace $popperPattern, ''
        $modified = $true
    }
    
    $commentPattern1 = '<!--\s*' + [regex]::Escape('Подключение') + '\s+.*?Bootstrap\s+JS\s*-->'
    if ($content -match $commentPattern1) {
        $matches = [regex]::Matches($content, $commentPattern1)
        $script:stats.comments_removed += $matches.Count
        $content = $content -replace $commentPattern1, ''
        $modified = $true
    }
    
    $commentPattern2 = '<!--\s*Bootstrap\s+JS\s+.*?-->'
    if ($content -match $commentPattern2) {
        $matches = [regex]::Matches($content, $commentPattern2)
        $script:stats.comments_removed += $matches.Count
        $content = $content -replace $commentPattern2, ''
        $modified = $true
    }
    
    $jqueryScriptPattern = '(?s)<script>\s*\$\(document\)\.ready\(.*?\);\s*</script>'
    if ($content -match $jqueryScriptPattern) {
        $matches = [regex]::Matches($content, $jqueryScriptPattern)
        $script:stats.jquery_scripts_removed += $matches.Count
        $content = $content -replace $jqueryScriptPattern, ''
        $modified = $true
    }
    
    $content = $content -replace '<p>\s*</p>\s*<p>\s*</p>', ''
    $content = $content -replace '<p>\s*</p>\s*$', ''
    
    if ($modified) {
        $backupPath = "$FilePath.backup"
        $originalContent | Out-File -FilePath $backupPath -Encoding UTF8 -NoNewline
        $content | Out-File -FilePath $FilePath -Encoding UTF8 -NoNewline
        $script:stats.files_modified++
        return $true
    }
    
    return $false
}

Write-Host ""
Write-Host "Removing jQuery and Bootstrap scripts..." -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $PAGES_DIR)) {
    Write-Host "Directory not found: $PAGES_DIR" -ForegroundColor Red
    exit 1
}

Write-Host "Searching for markdown files in: $PAGES_DIR" -ForegroundColor Yellow
Write-Host ("=" * 80)

$mdFiles = Get-ChildItem -Path $PAGES_DIR -Recurse -Include "*.md"
Write-Host "Found files: $($mdFiles.Count)" -ForegroundColor Green
Write-Host ""

foreach ($file in $mdFiles) {
    $modified = Remove-ScriptsFromFile -FilePath $file.FullName
    if ($modified) {
        $relativePath = $file.FullName.Replace($PAGES_DIR, "").TrimStart("\")
        Write-Host "Modified: $relativePath" -ForegroundColor Green
    }
}

Write-Host ("")
Write-Host ("=" * 80)
Write-Host "STATISTICS" -ForegroundColor Cyan
Write-Host ("=" * 80)
Write-Host "Files processed:          $($stats.files_processed)"
Write-Host "Files modified:           $($stats.files_modified)"
Write-Host ""
Write-Host "jQuery removed:           $($stats.jquery_removed)"
Write-Host "Bootstrap JS removed:     $($stats.bootstrap_removed)"
Write-Host "Popper.js removed:        $($stats.popper_removed)"
Write-Host "Comments removed:         $($stats.comments_removed)"
Write-Host "jQuery scripts removed:   $($stats.jquery_scripts_removed)"
Write-Host ("=" * 80)

if ($stats.files_modified -gt 0) {
    Write-Host ""
    Write-Host "Backup files saved with .backup extension" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Green
Write-Host ""
