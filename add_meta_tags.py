#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление SEO мета-тегов в Markdown файлы Grav CMS
Оптимизация для российского рынка: Яндекс, VK, Russian locale
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# Конфигурация
PAGES_DIR = r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"
SITE_URL = "https://service04.ru"
SITE_NAME = "Service04"
SITE_LOCALE = "ru_RU"
DEFAULT_OG_IMAGE = "/images/og-default.jpg"
BACKUP_EXTENSION = ".bak"
REPORT_FILE = "meta_tags_report.txt"

# Статистика
stats = {
    'files_processed': 0,
    'files_modified': 0,
    'meta_added': 0,
    'descriptions_generated': 0
}

def clean_html(text):
    """Удаляет HTML теги из текста"""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def generate_description(content, max_length=155):
    """
    Генерирует описание из контента страницы
    Оптимальная длина для Яндекс и Google: 150-160 символов
    """
    # Удаляем frontmatter
    content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
    
    # Удаляем <style> блоки
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Удаляем <script> блоки
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Удаляем HTML комментарии
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Удаляем HTML теги
    text = clean_html(content)
    
    # Удаляем лишние пробелы и переносы строк
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Извлекаем первые предложения
    sentences = re.split(r'[.!?]\s+', text)
    
    description = ""
    for sentence in sentences:
        sentence = sentence.strip()
        # Пропускаем короткие фразы и CSS/JS артефакты
        if len(sentence) < 15 or '{' in sentence or '}' in sentence:
            continue
        if len(description) + len(sentence) > max_length:
            break
        description += sentence + ". "
    
    description = description.strip()
    
    # Если описание слишком короткое, берем первый параграф
    if len(description) < 50 and len(text) > 50:
        # Ищем первый параграф (текст между <p> или после заголовка)
        paragraph_match = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL | re.IGNORECASE)
        if paragraph_match:
            para_text = clean_html(paragraph_match.group(1))
            description = para_text[:max_length] + "..."
        else:
            description = text[:max_length] + "..."
    
    # Финальная обрезка
    if len(description) > max_length:
        description = description[:max_length].rsplit(' ', 1)[0] + "..."
    
    return description if description else "Профессиональный ремонт котельного оборудования в Москве и МО"

def extract_first_image(content):
    """Извлекает первое изображение из контента"""
    # Поиск <img src="...">
    img_match = re.search(r'<img[^>]+src=["\'](.*?)["\']', content, re.IGNORECASE)
    if img_match:
        img_src = img_match.group(1)
        # Пропускаем .svg и маленькие иконки
        if not img_src.endswith('.svg') and 'icon' not in img_src.lower():
            return img_src
    
    # Поиск ![alt](image.jpg)
    md_img_match = re.search(r'!\[.*?\]\((.*?)\)', content)
    if md_img_match:
        return md_img_match.group(1)
    
    return None

def get_page_path(file_path, pages_dir):
    """Конвертирует путь к файлу в URL путь"""
    rel_path = os.path.relpath(file_path, pages_dir)
    
    # Удаляем номера из папок (01.home -> home)
    parts = Path(rel_path).parts
    url_parts = []
    
    for part in parts[:-1]:  # Пропускаем default.md
        # Убираем номера типа "01."
        clean_part = re.sub(r'^\d+\.', '', part)
        url_parts.append(clean_part)
    
    # Формируем URL
    if not url_parts or url_parts[0] == 'home':
        return "/"
    
    return "/" + "/".join(url_parts)

def determine_og_type(path):
    """Определяет тип контента для og:type"""
    if 'blog' in path or 'kody-oshibok' in path or 'zapchasti' in path:
        return 'article'
    return 'website'

def add_meta_tags(file_path):
    """Добавляет SEO мета-теги в markdown файл"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        stats['files_processed'] += 1
        
        # Парсинг frontmatter
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        if not frontmatter_match:
            # Skip file without frontmatter (avoid encoding issues)
            return False
        
        frontmatter_text = frontmatter_match.group(1)
        body_content = frontmatter_match.group(2)
        
        # Загрузка YAML
        try:
            frontmatter = yaml.safe_load(frontmatter_text) or {}
        except yaml.YAMLError as e:
            # Skip YAML error files (avoid encoding issues)
            return False
        
        # Получаем title
        title = frontmatter.get('title', 'Service04')
        
        # Проверяем наличие metadata
        if 'metadata' not in frontmatter:
            frontmatter['metadata'] = {}
        
        metadata = frontmatter['metadata']
        
        # Проверяем нужно ли обновлять (пропускаем только если og:title есть И description хороший)
        has_og = 'og:title' in metadata
        has_good_description = 'description' in metadata and metadata['description']
        if has_good_description:
            desc = metadata['description']
            # Плохое описание если содержит CSS/JS артефакты
            has_good_description = '{' not in desc and '}' not in desc and len(desc) > 30
        
        if has_og and has_good_description:
            return False
        
        # Генерируем описание
        if 'description' not in metadata or not metadata['description']:
            description = generate_description(body_content)
            metadata['description'] = description
            stats['descriptions_generated'] += 1
        else:
            description = metadata['description']
            # Проверяем если описание содержит артефакты CSS/JS - регенерируем
            if '{' in description or '}' in description or len(description) < 30:
                description = generate_description(body_content)
                metadata['description'] = description
                stats['descriptions_generated'] += 1
        
        # Определяем URL
        page_path = get_page_path(file_path, PAGES_DIR)
        canonical_url = SITE_URL + page_path
        
        # Поиск изображения
        og_image = extract_first_image(body_content)
        if og_image:
            # Конвертируем относительный путь в абсолютный
            if not og_image.startswith('http'):
                if not og_image.startswith('/'):
                    # Относительный путь - берем путь страницы
                    page_dir = os.path.dirname(page_path)
                    og_image = f"{page_dir}/{og_image}" if page_dir != '/' else f"/{og_image}"
            og_image_full = og_image if og_image.startswith('http') else SITE_URL + og_image
        else:
            og_image_full = SITE_URL + DEFAULT_OG_IMAGE
        
        # Определяем тип
        og_type = determine_og_type(page_path)
        
        # ===== РОССИЙСКАЯ ЛОКАЛИЗАЦИЯ =====
        
        # Open Graph (для VK, OK.ru)
        metadata['og:type'] = og_type
        metadata['og:title'] = f"{title} - {SITE_NAME}"
        metadata['og:description'] = description
        metadata['og:url'] = canonical_url
        metadata['og:site_name'] = SITE_NAME
        metadata['og:locale'] = SITE_LOCALE
        metadata['og:image'] = og_image_full
        metadata['og:image:width'] = '1200'
        metadata['og:image:height'] = '630'
        
        # Canonical URL
        metadata['canonical'] = canonical_url
        
        # Robots (для Яндекс и Google)
        metadata['robots'] = 'index, follow'
        
        # Яндекс специфичные теги
        metadata['yandex-verification'] = ''  # Пользователь может заполнить позже
        
        # Дополнительные теги для России
        metadata['geo.region'] = 'RU-MOW'  # Москва
        metadata['geo.placename'] = 'Москва'
        
        # Author
        metadata['author'] = SITE_NAME
        
        stats['meta_added'] += 1
        stats['files_modified'] += 1
        
        # Сохраняем обратно в frontmatter
        frontmatter['metadata'] = metadata
        
        # Конвертируем обратно в YAML
        new_frontmatter = yaml.dump(frontmatter, 
                                    allow_unicode=True,
                                    default_flow_style=False,
                                    sort_keys=False)
        
        # Собираем файл
        new_content = f"---\n{new_frontmatter}---\n{body_content}"
        
        # Создаем backup
        backup_path = str(file_path) + BACKUP_EXTENSION
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Записываем новый контент
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        # Skip error files (avoid encoding issues)
        return False

def find_markdown_files(directory):
    """Рекурсивно находит все .md файлы"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and not file.endswith('.bak'):
                md_files.append(os.path.join(root, file))
    return md_files

def generate_report(modified_files):
    """Генерирует отчет о добавленных мета-тегах"""
    report_path = os.path.join(os.path.dirname(PAGES_DIR), REPORT_FILE)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("Отчет о добавлении SEO мета-тегов\n")
        f.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Обработано файлов: {stats['files_processed']}\n")
        f.write(f"Изменено файлов: {stats['files_modified']}\n")
        f.write(f"Добавлено мета-тегов: {stats['meta_added']}\n")
        f.write(f"Сгенерировано описаний: {stats['descriptions_generated']}\n\n")
        
        if modified_files:
            f.write("\nИзмененные файлы:\n")
            f.write("-" * 70 + "\n")
            for file_path in modified_files:
                rel_path = os.path.relpath(file_path, PAGES_DIR)
                f.write(f"{rel_path}\n")
        
        # Примеры добавленных тегов
        f.write("\n\nПримеры добавленных мета-тегов:\n")
        f.write("-" * 70 + "\n")
        f.write("""
metadata:
    description: 'Автоматически сгенерированное описание...'
    og:type: 'website'
    og:title: 'Название страницы - Service04'
    og:description: 'Описание для соцсетей'
    og:url: 'https://service04.ru/path'
    og:site_name: 'Service04'
    og:locale: 'ru_RU'
    og:image: 'https://service04.ru/image.jpg'
    og:image:width: '1200'
    og:image:height: '630'
    canonical: 'https://service04.ru/path'
    robots: 'index, follow'
    yandex-verification: ''
    geo.region: 'RU-MOW'
    geo.placename: 'Москва'
    author: 'Service04'
""")
    
    return report_path

def main():
    """Основная функция"""
    print("=" * 70)
    print("[SEO] Добавление мета-тегов для российского рынка")
    print("=" * 70)
    print()
    
    if not os.path.exists(PAGES_DIR):
        print(f"[ОШИБКА] Директория не найдена: {PAGES_DIR}")
        return
    
    # Находим все markdown файлы
    print(f"[ПОИСК] Сканирование: {PAGES_DIR}")
    md_files = find_markdown_files(PAGES_DIR)
    print(f"[OK] Найдено {len(md_files)} markdown файлов")
    print()
    
    # Обрабатываем файлы
    print("[ПРОЦЕСС] Добавление мета-тегов...")
    modified_files = []
    
    for i, file_path in enumerate(md_files, 1):
        if add_meta_tags(file_path):
            modified_files.append(file_path)
            # Print progress only by numbers to avoid encoding issues
            if i % 20 == 0:
                print(f"[PROGRESS] {i}/{len(md_files)} files processed")
    
    print()
    print("=" * 70)
    print("[СТАТИСТИКА]")
    print("=" * 70)
    print(f"Обработано файлов:           {stats['files_processed']}")
    print(f"Изменено файлов:             {stats['files_modified']}")
    print(f"Добавлено мета-тегов:        {stats['meta_added']}")
    print(f"Сгенерировано описаний:      {stats['descriptions_generated']}")
    print()
    
    # Генерируем отчет
    report_path = generate_report(modified_files)
    print(f"[ОТЧЕТ] Сохранен: {report_path}")
    print()
    print("[OK] Готово!")
    print()
    print("[ИНФО] Российская локализация:")
    print("   - Локаль: ru_RU (для VK, OK.ru)")
    print("   - Регион: Москва (RU-MOW)")
    print("   - Open Graph для российских соцсетей")
    print("   - Подготовлено для Яндекс.Вебмастер")
    print()
    print("[ИНФО] Следующие шаги:")
    print("   1. Добавить Яндекс.Вебмастер verification код")
    print("   2. Создать OG изображение: /images/og-default.jpg (1200x630)")
    print("   3. Проверить в VK Sharing Debugger")
    print("   4. Настроить Яндекс.Метрику")

if __name__ == "__main__":
    main()
