# PowerShell Script for Image Optimization
# Optimizes all images in the Grav site

param(
    [string]$Directory = "user\pages",
    [int]$MaxWidth = 1200,
    [int]$Quality = 85,
    [switch]$DryRun = $false
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Image Optimization Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Settings:" -ForegroundColor Yellow
Write-Host "  Directory: $Directory" -ForegroundColor Gray
Write-Host "  Max Width: $MaxWidth px" -ForegroundColor Gray
Write-Host "  Quality: $Quality%" -ForegroundColor Gray
Write-Host "  Dry Run: $DryRun" -ForegroundColor Gray
Write-Host ""

$imageExtensions = @("*.jpg", "*.jpeg", "*.png")
$optimized = 0
$skipped = 0
$totalOriginalSize = 0
$totalNewSize = 0
$errors = 0

foreach ($ext in $imageExtensions) {
    $images = Get-ChildItem -Path $Directory -Filter $ext -Recurse -File
    
    foreach ($image in $images) {
        try {
            $originalSize = $image.Length
            $totalOriginalSize += $originalSize
            
            # Skip very small images (likely already optimized or icons)
            if ($originalSize -lt 10KB) {
                $skipped++
                Write-Host "[SKIP] $($image.Name) - too small ($([math]::Round($originalSize/1KB, 2)) KB)" -ForegroundColor DarkGray
                continue
            }
            
            if ($DryRun) {
                Write-Host "[DRY RUN] Would optimize: $($image.Name)" -ForegroundColor Yellow
                $optimized++
            }
            else {
                # Create backup
                $backupPath = $image.FullName + ".bak"
                Copy-Item $image.FullName $backupPath -Force
                
                # Optimize image
                $outputPath = $image.FullName
                
                & magick $image.FullName `
                    -resize "${MaxWidth}x>" `
                    -quality $Quality `
                    -strip `
                    -interlace Plane `
                    -sampling-factor 4:2:0 `
                    $outputPath
                
                if ($LASTEXITCODE -eq 0) {
                    $newSize = (Get-Item $outputPath).Length
                    $totalNewSize += $newSize
                    $saved = $originalSize - $newSize
                    
                    if ($saved -gt 0) {
                        $percent = [math]::Round(($saved / $originalSize) * 100, 2)
                        $savedKB = [math]::Round($saved / 1KB, 2)
                        Write-Host "[OK] $($image.Name): -$percent% (-$savedKB KB)" -ForegroundColor Green
                        $optimized++
                        
                        # Remove backup on success
                        Remove-Item $backupPath -Force
                    }
                    else {
                        # Image got bigger, restore backup
                        Move-Item $backupPath $image.FullName -Force
                        $skipped++
                        Write-Host "[SKIP] $($image.Name) - optimization increased size" -ForegroundColor Yellow
                    }
                }
                else {
                    # Error occurred, restore backup
                    if (Test-Path $backupPath) {
                        Move-Item $backupPath $image.FullName -Force
                    }
                    $errors++
                    Write-Host "[ERROR] $($image.Name) - optimization failed" -ForegroundColor Red
                }
            }
        }
        catch {
            $errors++
            Write-Host "[ERROR] $($image.Name) - $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Optimization Complete!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Statistics:" -ForegroundColor Yellow
Write-Host "  Optimized: $optimized images" -ForegroundColor Green
Write-Host "  Skipped: $skipped images" -ForegroundColor Gray
Write-Host "  Errors: $errors images" -ForegroundColor $(if ($errors -gt 0) { "Red" } else { "Gray" })

if (-not $DryRun -and $optimized -gt 0) {
    $totalSaved = $totalOriginalSize - $totalNewSize
    $totalSavedMB = [math]::Round($totalSaved / 1MB, 2)
    $overallPercent = [math]::Round(($totalSaved / $totalOriginalSize) * 100, 2)
    
    Write-Host ""
    Write-Host "Space Saved:" -ForegroundColor Yellow
    Write-Host "  Total: $totalSavedMB MB ($overallPercent%)" -ForegroundColor Green
    Write-Host "  Original: $([math]::Round($totalOriginalSize/1MB, 2)) MB" -ForegroundColor Gray
    Write-Host "  New: $([math]::Round($totalNewSize/1MB, 2)) MB" -ForegroundColor Gray
}

Write-Host ""
