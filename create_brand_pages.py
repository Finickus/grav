import os
import re
from pathlib import Path

# Базовый путь к папке с кодами ошибок
base_path = Path(r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages\08.kody-oshibok")

# Функция для преобразования имени папки в читаемый заголовок
def format_title(folder_name):
    title = folder_name.replace('-', ' ')
    # Убираем префиксы
    title = re.sub(r'^kody oshibok ', '', title)
    title = re.sub(r'^oshibka ', 'Ошибка ', title)
    title = re.sub(r'^oshibki ', 'Ошибки ', title)
    return title.title()

# Получить список брендов
brands = [d for d in base_path.iterdir() if d.is_dir() and not d.name.startswith('.')]

created_count = 0

for brand_dir in brands:
    brand_name = brand_dir.name
    brand_title = brand_name.capitalize()
    
    # Получить список подпапок
    subfolders = [d for d in brand_dir.iterdir() if d.is_dir()]
    
    if not subfolders:
        print(f"⚠ {brand_name} - нет подпапок, пропускаю")
        continue
    
    # Определить цвет и иконку для карточек
    cards_html = ""
    for subfolder in subfolders:
        subfolder_name = subfolder.name
        page_title = format_title(subfolder_name)
        
        # Определить иконку и цвет
        if re.search(r'oshibka|error|e\d+|f\d+', subfolder_name, re.I):
            icon = "fas fa-exclamation-circle"
            bg_color = "danger"
        elif re.search(r'kody-oshibok|codes', subfolder_name, re.I):
            icon = "fas fa-list-alt"
            bg_color = "info"
        else:
            icon = "fas fa-file-alt"
            bg_color = "primary"
        
        cards_html += f"""
        <div class="col-md-6 col-lg-4">
            <a href="{brand_name}/{subfolder_name}" class="text-decoration-none">
                <div class="card h-100 border-0 shadow-sm hover-lift transition">
                    <div class="card-body p-4">
                        <div class="d-flex align-items-start mb-3">
                            <div class="bg-{bg_color} bg-opacity-10 rounded p-3 me-3" style="min-width: 60px; height: 60px; display: flex; align-items: center; justify-content: center;">
                                <i class="{icon} text-{bg_color} fa-2x"></i>
                            </div>
                            <div class="flex-grow-1">
                                <h5 class="h6 fw-bold text-dark mb-2">{page_title}</h5>
                                <p class="small text-muted mb-0">Подробная информация</p>
                            </div>
                        </div>
                        <div class="text-end">
                            <span class="small text-{bg_color} fw-bold">Подробнее <i class="fas fa-arrow-right ms-1"></i></span>
                        </div>
                    </div>
                </div>
            </a>
        </div>
"""
    
    # Создать содержимое файла
    content = f"""---
title: Коды ошибок котлов {brand_title}
process:
  twig: true
  markdown: false
metadata:
  description: Полный справочник кодов ошибок котлов {brand_title}. Расшифровка, причины возникновения и способы устранения неисправностей.
  og:type: article
  og:title: Коды ошибок котлов {brand_title} - Service04
  og:description: Полный справочник кодов ошибок котлов {brand_title}. Расшифровка, причины возникновения и способы устранения неисправностей.
  огurl: https://service04.ru/kody-oshibok/{brand_name}
  og:site_name: Service04
  og:locale: ru_RU
  og:image: https://service04.ru/images/og-default.jpg
  og:image:width: '1200'
  og:image:height: '630'
  canonical: https://service04.ru/kody-oshibok/{brand_name}
  robots: index, follow
  yandex-verification: ''
  geo.region: RU-MOW
  geo.placename: Москва
  author: Service04
---
<div class="container py-5">
    
    <div class="p-5 mb-5 text-white text-center rounded-3 shadow-lg" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
        <h1 class="display-5 fw-bold">
            <i class="fas fa-exclamation-triangle me-3"></i>Коды ошибок котлов {brand_title}
        </h1>
        <p class="lead">Выберите модель или тип ошибки для получения подробной информации</p>
    </div>

    <div class="card shadow-lg border-0 mb-5">
        <div class="card-body p-4 p-md-5">
            <h2 class="h4 fw-bold mb-4 text-primary border-bottom pb-3">
                <i class="fas fa-info-circle me-2"></i>О кодах ошибок {brand_title}
            </h2>
            <p class="small mb-3">
                Котлы {brand_title} оснащены современной системой самодиагностики, которая при возникновении неисправности выводит на дисплей соответствующий код ошибки. Понимание этих кодов позволяет быстро определить причину поломки и принять необходимые меры для её устранения.
            </p>
            <p class="small mb-0">
                Ниже представлены все доступные разделы с подробной информацией о кодах ошибок для котлов {brand_title}.
            </p>
        </div>
    </div>

    <div class="row g-4">
{cards_html}
    </div>

    <style>
        .hover-lift {{
            transition: all 0.3s ease;
        }}
        .hover-lift:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.15) !important;
        }}
    </style>

    <div class="p-5 mt-5 rounded-3 text-center text-white bg-success bg-gradient shadow-lg">
        <h3 class="h4 mb-3"><i class="fas fa-phone-alt me-2"></i>Нужна помощь с ремонтом?</h3>
        <p class="lead mb-4">Наши специалисты помогут быстро устранить любую неисправность котла {brand_title}. Работаем круглосуточно!</p>
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
"""
    
    # Записать файл
    default_md = brand_dir / "default.md"
    default_md.write_text(content, encoding='utf-8')
    created_count += 1
    print(f"✓ {brand_name} - создана страница ({len(subfolders)} разделов)")

print(f"\n✅ Создано промежуточных страниц: {created_count}")
