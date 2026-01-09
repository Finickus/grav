# PowerShell скрипт для создания промежуточных страниц брендов
# Создает default.md в каждой папке бренда со ссылками на подстраницы

$basePath = "c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages\08.kody-oshibok"
$brands = Get-ChildItem -Path $basePath -Directory | Where-Object { $_.Name -notmatch '^\d+\.' }

foreach ($brand in $brands) {
    $brandName = $brand.Name
    $brandPath = $brand.FullName
    $defaultMd = Join-Path $brandPath "default.md"
    
    # Получить список подпапок (страниц)
    $subfolders = Get-ChildItem -Path $brandPath -Directory
    
    if ($subfolders.Count -eq 0) {
        Write-Host "⚠ $brandName - нет подпапок, пропускаем" -ForegroundColor Yellow
        continue
    }
    
    # Преобразовать имя бренда в читаемое название
    $brandTitle = (Get-Culture).TextInfo.ToTitleCase($brandName)
    
    # Создать YAML заголовок
    $yaml = @"
---
title: Коды ошибок котлов $brandTitle
process:
  twig: true
  markdown: false
metadata:
  description: Полный справочник кодов ошибок котлов $brandTitle. Расшифровка, причины возникновения и способы устранения неисправностей.
  og:type: article
  og:title: Коды ошибок котлов $brandTitle - Service04
  og:description: Полный справочник кодов ошибок котлов $brandTitle. Расшифровка, причины возникновения и способы устранения неисправностей.
  og:url: https://service04.ru/kody-oshibok/$brandName
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/images/og-default.jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/kody-oshibok/$brandName
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
"@
    
    # Создать HTML контент
    $html = @"
<div class="container py-5">
    
    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-lg" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Коды ошибок котлов $brandTitle
        </h1>
        <p class="lead">Выберите модель или тип ошибки для получения подробной информации</p>
    </div>

    <div class="card shadow-lg border-0 mb-5">
        <div class="card-body p-4 p-md-5">
            <h2 class="h4 fw-bold mb-4 text-primary border-bottom pb-3">
                <i class="fas fa-info-circle me-2"></i>О кодах ошибок $brandTitle
            </h2>
            <p class="small mb-3">
                Котлы $brandTitle оснащены современной системой самодиагностики, которая при возникновении неисправности выводит на дисплей соответствующий код ошибки. Понимание этих кодов позволяет быстро определить причину поломки и принять необходимые меры для её устранения.
            </p>
            <p class="small mb-0">
                Ниже представлены все доступные разделы с подробной информацией о кодах ошибок для котлов $brandTitle.
            </p>
        </div>
    </div>

    <div class="row g-4">
"@
    
    # Добавить карточки для каждой подпапки
    foreach ($subfolder in $subfolders) {
        $subfolderName = $subfolder.Name
        # Преобразовать имя папки в читаемый заголовок
        $pageTitle = $subfolderName -replace '-', ' ' -replace '^kody oshibok ', '' `
            -replace '^oshibka ', 'Ошибка ' -replace '^oshibki ', 'Ошибки '
        $pageTitle = (Get-Culture).TextInfo.ToTitleCase($pageTitle)
        
        # Определить иконку и цвет на основе имени
        $icon = "fas fa-file-alt"
        $bgColor = "primary"
        
        if ($subfolderName -match 'oshibka|error|e\d+|f\d+') {
            $icon = "fas fa-exclamation-circle"
            $bgColor = "danger"
        }
        elseif ($subfolderName -match 'kody-oshibok|codes') {
            $icon = "fas fa-list-alt"
            $bgColor = "info"
        }
        
        $html += @"

        <div class="col-md-6 col-lg-4">
            <a href="$brandName/$subfolderName" class="text-decoration-none">
                <div class="card h-100 border-0 shadow-sm hover-lift transition">
                    <div class="card-body p-4">
                        <div class="d-flex align-items-start mb-3">
                            <div class="bg-$bgColor bg-opacity-10 rounded p-3 me-3" style="min-width: 60px; height: 60px; display: flex; align-items: center; justify-content: center;">
                                <i class="$icon text-$bgColor fa-2x"></i>
                            </div>
                            <div class="flex-grow-1">
                                <h5 class="h6 fw-bold text-dark mb-2">$pageTitle</h5>
                                <p class="small text-muted mb-0">Подробная информация</p>
                            </div>
                        </div>
                        <div class="text-end">
                            <span class="small text-$bgColor fw-bold">Подробнее <i class="fas fa-arrow-right ms-1"></i></span>
                        </div>
                    </div>
                </div>
            </a>
        </div>
"@
    }
    
    # Закрыть контейнер и добавить стили + CTA
    $html += @"

    </div>

    <style>
        .hover-lift {
            transition: all 0.3s ease;
        }
        .hover-lift:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15) !important;
        }
    </style>

    <div class="p-5 mt-5 rounded-3 text-center text-white bg-success bg-gradient shadow-lg">
        <h3 class="h4 mb-3"><i class="fas fa-phone-alt me-2"></i>Нужна помощь с ремонтом?</h3>
        <p class="lead mb-4">Наши специалисты помогут быстро устранить любую неисправность котла $brandTitle. Работаем круглосуточно!</p>
        <div class="row justify-content-center g-3">
            <div class="col-12 col-md-4">
                <a href="tel:+79262211348" class="btn btn-light btn-lg w-100 fw-bold">
                    <i class="fas fa-phone me-2"></i> Позвонить
                </a>
            </div>
            <div class="col-12 col-md-4">
                <a href="https://service04.ru/contact-us/feedback" class="btn btn-warning btn-lg w-100 fw-bold text-dark">
                    <i class="fas fa-envelope me-2"></i> Оставить заявку
                </a>
            </div>
        </div>
    </div>

</div>
"@
    
    # Объединить YAML и HTML
    $content = $yaml + "`r`n" + $html
    
    # Записать файл
    Set-Content -Path $defaultMd -Value $content -Encoding UTF8
    Write-Host "✓ Создана страница для $brandName ($($subfolders.Count) разделов)" -ForegroundColor Green
}

Write-Host "`n✅ Готово! Создано промежуточных страниц: $($brands.Count)" -ForegroundColor Cyan
"@
