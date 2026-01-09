# Script for automatic replacement of FontAwesome icons with SVG
# For all Grav site pages

param(
    [string]$PagesDir = "user\pages"
)

$filesProcessed = 0
$replacementsMade = 0

function Replace-Icons {
    param ([string]$filePath)
    
    try {
        $content = Get-Content $filePath -Raw -Encoding UTF8
        $originalContent = $content
        
        # Replace check icons
        $content = $content -replace '<i class="fas fa-check-circle([^"]*)">\s*</i>', '<img src="/home/check-circle.svg" alt="" class="me-2" style="width: 20px; height: 20px; vertical-align: middle;">'
        $content = $content -replace '<i class="fas fa-check-double([^"]*)">\s*</i>', '<img src="/home/check-circle.svg" alt="" class="me-2" style="width: 20px; height: 20px; vertical-align: middle;">'
        $content = $content -replace '<i class="fas fa-check([^"]*)">\s*</i>', '<img src="/home/check.svg" alt="" class="me-2" style="width: 18px; height: 18px; vertical-align: middle;">'
        
        # Replace social media icons
        $content = $content -replace '<i class="fab fa-telegram-plane([^"]*)">\s*</i>', '<img src="/home/telegram.svg" alt="Telegram" style="width: 24px; height: 24px; vertical-align: middle;">'
        $content = $content -replace '<i class="fab fa-telegram([^"]*)">\s*</i>', '<img src="/home/telegram.svg" alt="Telegram" style="width: 24px; height: 24px; vertical-align: middle;">'
        $content = $content -replace '<i class="fab fa-whatsapp([^"]*)">\s*</i>', '<img src="/home/whatsapp.svg" alt="WhatsApp" style="width: 24px; height: 24px; vertical-align: middle;">'
        $content = $content -replace '<i class="fab fa-vk([^"]*)">\s*</i>', '<img src="/home/vk.svg" alt="VK" style="width: 24px; height: 24px; vertical-align: middle;">'
        
        if ($content -ne $originalContent) {
            Set-Content -Path $filePath -Value $content -Encoding UTF8 -NoNewline
            return $true
        }
    }
    catch {
        Write-Host "Error processing file: $filePath" -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red
    }
    
    return $false
}

# Get all .md files
$mdFiles = Get-ChildItem -Path $PagesDir -Filter "*.md" -Recurse

Write-Host "Found $($mdFiles.Count) .md files" -ForegroundColor Cyan
Write-Host "Processing files..." -ForegroundColor Cyan
Write-Host ""

foreach ($file in $mdFiles) {
    $filesProcessed++
    
    if (Replace-Icons -filePath $file.FullName) {
        $replacementsMade++
        $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "")
        Write-Host "[OK] $relativePath" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "========================================"  -ForegroundColor Cyan
Write-Host "Processing complete!" -ForegroundColor Green
Write-Host "Files processed: $filesProcessed" -ForegroundColor Yellow
Write-Host "Files modified: $replacementsMade" -ForegroundColor Yellow
Write-Host "========================================"  -ForegroundColor Cyan
