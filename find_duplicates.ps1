param(
    [string]$PagesDir = "c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"
)

# Найти все markdown файлы
$mdFiles = Get-ChildItem -Path $PagesDir -Filter "*.md" -Recurse

Write-Host "Найдено файлов: $($mdFiles.Count)" -ForegroundColor Green
Write-Host "`nАнализ страниц..." -ForegroundColor Yellow

# Массивы для хранения данных
$pages = @()

foreach ($file in $mdFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Извлечь title из frontmatter
    $title = ""
    if ($content -match "(?ms)^---\s*$(.*?)^---") {
        $frontmatter = $matches[1]
        if ($frontmatter -match "title:\s*[`"']?(.+?)[`"']?\s*$") {
            $title = $matches[1].Trim('"', "'")
        }
    }
    
    # Извлечь основное содержимое (без frontmatter)
    $bodyContent = $content -replace "(?ms)^---\s*$.*?^---\s*$", ""
    $bodyContent = $bodyContent.Trim()
    
    # Вычислить хеш содержимого
    $contentHash = ($bodyContent | Get-FileHash -Algorithm MD5 -InputStream ([System.IO.MemoryStream]::new([System.Text.Encoding]::UTF8.GetBytes($_)))).Hash
    
    $pages += [PSCustomObject]@{
        Path = $file.FullName
        RelativePath = $file.FullName.Replace($PagesDir + "\", "")
        Title = $title
        ContentLength = $bodyContent.Length
        ContentHash = $contentHash
        Content = $bodyContent
    }
}

# Поиск дубликатов
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "РЕЗУЛЬТАТЫ ПОИСКА ДУБЛИКАТОВ" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# 1. Дубликаты по заголовкам
Write-Host "1. ДУБЛИКАТЫ ПО ЗАГОЛОВКАМ (title):" -ForegroundColor Yellow
$titleGroups = $pages | Where-Object { $_.Title -ne "" } | Group-Object -Property Title | Where-Object { $_.Count -gt 1 }
if ($titleGroups.Count -gt 0) {
    foreach ($group in $titleGroups) {
        Write-Host "`n  Заголовок: '$($group.Name)' (найдено: $($group.Count) страниц)" -ForegroundColor Red
        foreach ($page in $group.Group) {
            Write-Host "    - $($page.RelativePath)" -ForegroundColor White
        }
    }
} else {
    Write-Host "  Дубликатов по заголовкам не найдено." -ForegroundColor Green
}

# 2. Дубликаты по идентичному содержимому
Write-Host "`n2. ДУБЛИКАТЫ ПО ИДЕНТИЧНОМУ СОДЕРЖИМОМУ:" -ForegroundColor Yellow
$contentGroups = $pages | Group-Object -Property ContentHash | Where-Object { $_.Count -gt 1 }
if ($contentGroups.Count -gt 0) {
    foreach ($group in $contentGroups) {
        Write-Host "`n  Одинаковое содержимое (найдено: $($group.Count) страниц)" -ForegroundColor Red
        foreach ($page in $group.Group) {
            Write-Host "    - $($page.RelativePath) (title: '$($page.Title)')" -ForegroundColor White
        }
    }
} else {
    Write-Host "  Дубликатов по идентичному содержимому не найдено." -ForegroundColor Green
}

# 3. Очень похожие страницы (по длине содержимого с допуском 5%)
Write-Host "`n3. ОЧЕНЬ ПОХОЖИЕ СТРАНИЦЫ (одинаковая длина содержимого ±5%):" -ForegroundColor Yellow
$similarFound = $false
for ($i = 0; $i -lt $pages.Count; $i++) {
    for ($j = $i + 1; $j -lt $pages.Count; $j++) {
        $page1 = $pages[$i]
        $page2 = $pages[$j]
        
        if ($page1.ContentHash -ne $page2.ContentHash) {
            $lengthDiff = [Math]::Abs($page1.ContentLength - $page2.ContentLength)
            $avgLength = ($page1.ContentLength + $page2.ContentLength) / 2
            
            if ($avgLength -gt 0 -and ($lengthDiff / $avgLength) -lt 0.05) {
                if (-not $similarFound) {
                    $similarFound = $true
                }
                Write-Host "`n  Похожие страницы (разница в длине: $lengthDiff символов):" -ForegroundColor Red
                Write-Host "    - $($page1.RelativePath) (title: '$($page1.Title)', длина: $($page1.ContentLength))" -ForegroundColor White
                Write-Host "    - $($page2.RelativePath) (title: '$($page2.Title)', длина: $($page2.ContentLength))" -ForegroundColor White
            }
        }
    }
}
if (-not $similarFound) {
    Write-Host "  Очень похожих страниц не найдено." -ForegroundColor Green
}

# Сохранить отчет в файл
$reportPath = Join-Path $env:USERPROFILE ".gemini\antigravity\brain\8e84b854-e452-43bd-9519-19cb5c96994c\duplicate_pages_report.md"
$report = @"
# Отчет о поиске дубликатов страниц

**Дата анализа:** $(Get-Date -Format "dd.MM.yyyy HH:mm:ss")
**Всего проанализировано страниц:** $($pages.Count)

---

## 1. Дубликаты по заголовкам (title)

"@

if ($titleGroups.Count -gt 0) {
    foreach ($group in $titleGroups) {
        $report += "`n### Заголовок: ``$($group.Name)```n`n"
        $report += "**Найдено страниц:** $($group.Count)`n`n"
        foreach ($page in $group.Group) {
            $report += "- [$($page.RelativePath)](file:///$($page.Path.Replace('\', '/')))`n"
        }
    }
} else {
    $report += "`n*Дубликатов по заголовкам не найдено.*`n"
}

$report += "`n---`n`n## 2. Дубликаты по идентичному содержимому`n"

if ($contentGroups.Count -gt 0) {
    foreach ($group in $contentGroups) {
        $report += "`n### Группа дубликатов`n`n"
        $report += "**Найдено страниц с идентичным содержимым:** $($group.Count)`n`n"
        foreach ($page in $group.Group) {
            $report += "- [$($page.RelativePath)](file:///$($page.Path.Replace('\', '/'))) - *title:* ``$($page.Title)```n"
        }
    }
} else {
    $report += "`n*Дубликатов по идентичному содержимому не найдено.*`n"
}

$report += "`n---`n`n## 3. Очень похожие страницы (±5% по длине)`n"

$similarPairs = @()
for ($i = 0; $i -lt $pages.Count; $i++) {
    for ($j = $i + 1; $j -lt $pages.Count; $j++) {
        $page1 = $pages[$i]
        $page2 = $pages[$j]
        
        if ($page1.ContentHash -ne $page2.ContentHash) {
            $lengthDiff = [Math]::Abs($page1.ContentLength - $page2.ContentLength)
            $avgLength = ($page1.ContentLength + $page2.ContentLength) / 2
            
            if ($avgLength -gt 0 -and ($lengthDiff / $avgLength) -lt 0.05) {
                $similarPairs += [PSCustomObject]@{
                    Page1 = $page1
                    Page2 = $page2
                    LengthDiff = $lengthDiff
                }
            }
        }
    }
}

if ($similarPairs.Count -gt 0) {
    foreach ($pair in $similarPairs) {
        $report += "`n### Похожая пара страниц`n`n"
        $report += "**Разница в длине:** $($pair.LengthDiff) символов`n`n"
        $report += "- [$($pair.Page1.RelativePath)](file:///$($pair.Page1.Path.Replace('\', '/'))) - *title:* ``$($pair.Page1.Title)`` - *длина:* $($pair.Page1.ContentLength)`n"
        $report += "- [$($pair.Page2.RelativePath)](file:///$($pair.Page2.Path.Replace('\', '/'))) - *title:* ``$($pair.Page2.Title)`` - *длина:* $($pair.Page2.ContentLength)`n"
    }
} else {
    $report += "`n*Очень похожих страниц не найдено.*`n"
}

# Сохранить отчет
$report | Out-File -FilePath $reportPath -Encoding UTF8
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Отчет сохранен: $reportPath" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan
