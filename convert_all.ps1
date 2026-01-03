# PowerShell script for converting Bludit to Grav with Bootstrap 5
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'

# Bulma to Bootstrap 5 replacements
$replacements = @{
    'columns is-multiline'                 = 'row g-3'
    'columns is-centered'                  = 'row justify-content-center'
    'columns is-vcentered'                 = 'row align-items-center'
    'columns is-mobile'                    = 'row'
    'columns'                              = 'row'
    'column is-12-mobile'                  = 'col-12'
    'column is-6-mobile'                   = 'col-6'
    'column is-4-mobile'                   = 'col-4'
    'column is-half-mobile'                = 'col-6'
    'column is-12-tablet'                  = 'col-md-12'
    'column is-6-tablet'                   = 'col-md-6'
    'column is-4-tablet'                   = 'col-md-4'
    'column is-3-tablet'                   = 'col-md-3'
    'column is-half-tablet'                = 'col-md-6'
    'column is-12-desktop'                 = 'col-lg-12'
    'column is-8-desktop'                  = 'col-lg-8'
    'column is-6-desktop'                  = 'col-lg-6'
    'column is-5-desktop'                  = 'col-lg-5'
    'column is-4-desktop'                  = 'col-lg-4'
    'column is-3-desktop'                  = 'col-lg-3'
    'column is-half-desktop'               = 'col-lg-6'
    'column is-one-third-desktop'          = 'col-lg-4'
    'column is-one-sixth-desktop'          = 'col-lg-2'
    'column is-12'                         = 'col-12'
    'column is-8'                          = 'col-8'
    'column is-7'                          = 'col-7'
    'column is-6'                          = 'col-6'
    'column is-5'                          = 'col-5'
    'column is-4'                          = 'col-4'
    'column is-half'                       = 'col-6'
    'column is-one-third'                  = 'col-4'
    'column'                               = 'col'
    'container is-widescreen'              = 'container-fluid'
    'container'                            = 'container'
    'hero is-primary'                      = 'bg-primary text-white'
    'hero is-info'                         = 'bg-info text-white'
    'hero is-success'                      = 'bg-success text-white'
    'hero is-warning'                      = 'bg-warning text-dark'
    'hero is-danger'                       = 'bg-danger text-white'
    'hero is-light'                        = 'bg-light'
    'hero is-dark'                         = 'bg-dark text-white'
    'hero-body'                            = 'py-5'
    'box'                                  = 'card'
    'card-content'                         = 'card-body'
    'card-header-title'                    = 'card-title'
    'button is-primary'                    = 'btn btn-primary'
    'button is-info'                       = 'btn btn-info'
    'button is-success'                    = 'btn btn-success'
    'button is-warning'                    = 'btn btn-warning'
    'button is-danger'                     = 'btn btn-danger'
    'button is-light'                      = 'btn btn-light'
    'button is-dark'                       = 'btn btn-dark'
    'button is-secondary'                  = 'btn btn-secondary'
    'button'                               = 'btn btn-primary'
    ' is-large'                            = ' btn-lg'
    ' is-small'                            = ' btn-sm'
    ' is-fullwidth'                        = ' w-100'
    'title is-1'                           = 'h1 display-1'
    'title is-2'                           = 'h2 display-2'
    'title is-3'                           = 'h3 display-3'
    'title is-4'                           = 'h4 display-4'
    'title is-5'                           = 'h5'
    'title is-6'                           = 'h6'
    'title'                                = 'h3'
    'subtitle is-4'                        = 'h4 lead'
    'subtitle is-5'                        = 'h5 lead'
    'subtitle'                             = 'lead'
    'is-size-1'                            = 'fs-1'
    'is-size-2'                            = 'fs-2'
    'is-size-3'                            = 'fs-3'
    'is-size-4'                            = 'fs-4'
    'is-size-5'                            = 'fs-5'
    'is-size-6'                            = 'fs-6'
    'is-size-7'                            = 'fs-6'
    'has-text-centered'                    = 'text-center'
    'has-text-left'                        = 'text-start'
    'has-text-right'                       = 'text-end'
    'has-text-white'                       = 'text-white'
    'has-text-black'                       = 'text-dark'
    'has-text-dark'                        = 'text-dark'
    'has-text-primary'                     = 'text-primary'
    'has-text-info'                        = 'text-info'
    'has-text-success'                     = 'text-success'
    'has-text-warning'                     = 'text-warning'
    'has-text-danger'                      = 'text-danger'
    'has-text-grey'                        = 'text-muted'
    'has-text-muted'                       = 'text-muted'
    'has-background-primary'               = 'bg-primary'
    'has-background-info'                  = 'bg-info'
    'has-background-success'               = 'bg-success'
    'has-background-warning'               = 'bg-warning'
    'has-background-danger'                = 'bg-danger'
    'has-background-light'                 = 'bg-light'
    'has-background-dark'                  = 'bg-dark'
    'has-background-white'                 = 'bg-white'
    'has-background-grey'                  = 'bg-secondary'
    'has-background-secondary'             = 'bg-secondary'
    'card-header has-background-primary'   = 'card-header bg-primary text-white'
    'card-header has-background-info'      = 'card-header bg-info text-white'
    'card-header has-background-success'   = 'card-header bg-success text-white'
    'card-header has-background-warning'   = 'card-header bg-warning text-dark'
    'card-header has-background-danger'    = 'card-header bg-danger text-white'
    'card-header has-background-dark'      = 'card-header bg-dark text-white'
    'card-header has-background-secondary' = 'card-header bg-secondary text-white'
    ' mb-6'                                = ' mb-5'
    ' mt-6'                                = ' mt-5'
    ' ml-0'                                = ' ms-0'
    ' ml-2'                                = ' ms-2'
    ' ml-3'                                = ' ms-3'
    ' ml-4'                                = ' ms-4'
    ' mr-2'                                = ' me-2'
    ' mr-3'                                = ' me-3'
    ' mr-4'                                = ' me-4'
    'is-flex'                              = 'd-flex'
    'is-flex-direction-column'             = 'flex-column'
    'is-align-items-center'                = 'align-items-center'
    'is-justify-content-center'            = 'justify-content-center'
    'is-rounded'                           = 'rounded'
    'is-bold'                              = 'fw-bold'
    'has-shadow'                           = 'shadow'
    ' has-shadow'                          = ' shadow'
    ' is-widescreen'                       = ''
    ' is-light'                            = ''
    ' is-unstyled'                         = ' list-unstyled'
}

Write-Host ""
Write-Host "Converting Bludit to Grav with Bootstrap 5..." -ForegroundColor Cyan
Write-Host ("=" * 60)
Write-Host ""

$basePath = "user\bludit"
$successCount = 0
$errorCount = 0

$files = Get-ChildItem -Path $basePath -Recurse -Filter "index.txt"
$totalFiles = $files.Count

Write-Host "Found $totalFiles files to convert" -ForegroundColor Yellow
Write-Host ""

foreach ($file in $files) {
    $folderName = Split-Path -Path $file.DirectoryName -Leaf
    
    try {
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        
        # Extract title
        $title = "Bez nazvaniya"
        $headingLevel = 0
        
        if ($content -match '<h1[^>]*>(.*?)</h1>') {
            $title = $matches[1] -replace '<[^>]+>', ''
            $title = $title.Trim()
            $headingLevel = 1
        }
        elseif ($content -match '<h2[^>]*>(.*?)</h2>') {
            $title = $matches[1] -replace '<[^>]+>', ''
            $title = $title.Trim()
            $headingLevel = 2
        }
        
        # Remove heading
        if ($headingLevel -gt 0) {
            $content = $content -replace "<h$headingLevel[^>]*>.*?</h$headingLevel>", ''
        }
        
        # Convert classes (sort by length)
        $sortedKeys = $replacements.Keys | Sort-Object { $_.Length } -Descending
        foreach ($key in $sortedKeys) {
            $content = $content.Replace($key, $replacements[$key])
        }
        
        # Create new content with frontmatter
        $newContent = "---`r`ntitle: '$title'`r`n---`r`n`r`n" + $content
        
        # Write file
        $newFilePath = Join-Path -Path $file.DirectoryName -ChildPath 'default.ru.md'
        [System.IO.File]::WriteAllText($newFilePath, $newContent, [System.Text.Encoding]::UTF8)
        
        $successCount++
        Write-Host "[OK] $folderName : $title" -ForegroundColor Green
    }
    catch {
        $errorCount++
        Write-Host "[ERROR] $folderName : $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host ("=" * 60)
Write-Host "Results:" -ForegroundColor Yellow
Write-Host "  Success: $successCount" -ForegroundColor Green
Write-Host "  Errors:  $errorCount" -ForegroundColor Red
Write-Host "  Total:   $($successCount + $errorCount)" -ForegroundColor Cyan
Write-Host ""
Write-Host "Conversion completed!" -ForegroundColor Green
Write-Host ""
