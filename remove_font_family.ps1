$rootPath = "user\pages"
$filesProcessed = 0

Write-Host "Starting font-family removal process..." -ForegroundColor Cyan

$files = Get-ChildItem -Path $rootPath -Include *.md, *.txt -Recurse -File

Write-Host "Found $($files.Count) files to process"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Pattern to remove font-family and everything until semicolon
    $content = $content -replace 'font-family:[^;]+;', ''
    
    # Pattern to remove font-family at end without semicolon (before quote)
    $content = $content -replace 'font-family:[^;''"""]+(?=[''"""])', ''
    
    # Remove ; font-family before quote
    $content = $content -replace ';\s*font-family:[^;''"""]+(?=[''"""])', ''
    
    # Clean double semicolons
    $content = $content -replace ';;+', ';'
    
    # Clean style with only semicolon
    $content = $content -replace 'style="";', ''
    $content = $content -replace "style='';", ''
    $content = $content -replace 'style=" ";', ''
    $content = $content -replace "style=' ';", ''
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        $filesProcessed++
        Write-Host "Processed: $($file.Name)"
    }
}

Write-Host "`nFiles processed: $filesProcessed" -ForegroundColor Green
