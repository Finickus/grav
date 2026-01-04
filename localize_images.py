#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для скачивания внешних изображений и обновления ссылок в markdown файлах Grav CMS
"""

import os
import sys
import re
import requests
from pathlib import Path
from urllib.parse import urlparse, unquote
import time

# Настройка вывода для Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Конфигурация
BASE_DIR = Path(r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages")
EXTERNAL_DOMAIN = "https://service04.ru/bl-content/uploads/"

def download_image(url, target_path):
    """
    Скачивает изображение по URL и сохраняет его в target_path
    """
    try:
        # Добавляем небольшую задержку, чтобы не перегружать сервер
        time.sleep(0.5)
        
        response = requests.get(url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        
        # Создаем директорию, если её нет
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Сохраняем файл
        with open(target_path, 'wb') as f:
            f.write(response.content)
        
        print(f"[OK] Downloaded: {url} -> {target_path.name}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to download {url}: {e}")
        return False

def extract_image_urls(content):
    """
    Извлекает все URL изображений из содержимого markdown/HTML файла
    """
    # Паттерны для поиска изображений
    patterns = [
        r'<img[^>]*src=["\']([^"\']*service04\.ru[^"\']*)["\']',  # HTML img tags
        r'!\[([^\]]*)\]\(([^)]*service04\.ru[^)]*)\)',  # Markdown images
        r'href=["\']([^"\']*service04\.ru/bl-content/uploads/[^"\']*\.(jpg|jpeg|png|gif|svg|webp|pdf))["\']',  # Links to files
    ]
    
    urls = []
    for pattern in patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Берем последнюю группу как URL
            url = match.group(len(match.groups()))
            if 'service04.ru' in url:
                urls.append(url)
    
    return list(set(urls))  # Удаляем дубликаты

def get_image_filename(url):
    """
    Извлекает имя файла из URL
    """
    parsed = urlparse(url)
    # Берем последнюю часть пути
    filename = os.path.basename(unquote(parsed.path))
    # Очищаем имя файла от недопустимых символов
    filename = re.sub(r'[<>:"|?*]', '_', filename)
    return filename

def process_markdown_file(md_file_path):
    """
    Обрабатывает один markdown файл: скачивает изображения и обновляет ссылки
    """
    print(f"\n[FILE] Processing: {md_file_path.relative_to(BASE_DIR)}")
    
    try:
        # Читаем содержимое файла
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Извлекаем URL изображений
        image_urls = extract_image_urls(content)
        
        if not image_urls:
            print("  No external images found")
            return 0
        
        print(f"  Found {len(image_urls)} images")
        
        # Директория страницы
        page_dir = md_file_path.parent
        
        # Счетчик успешно скачанных изображений
        downloaded_count = 0
        
        # Обновленное содержимое
        updated_content = content
        
        # Обрабатываем каждое изображение
        for url in image_urls:
            # Получаем имя файла
            filename = get_image_filename(url)
            
            # Путь для сохранения
            target_path = page_dir / filename
            
            # Скачиваем изображение (если его еще нет)
            if not target_path.exists():
                if download_image(url, target_path):
                    downloaded_count += 1
            else:
                print(f"  Already exists: {filename}")
                downloaded_count += 1
            
            # Обновляем ссылки в содержимом
            # Заменяем полный URL на относительный путь (просто имя файла)
            updated_content = updated_content.replace(url, filename)
        
        # Сохраняем обновленный файл
        if updated_content != content:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  [OK] File updated: {downloaded_count} images")
        
        return downloaded_count
        
    except Exception as e:
        print(f"  [ERROR] Failed to process file: {e}")
        return 0

def main():
    """
    Главная функция
    """
    print("=" * 80)
    print("Localizing external images in Grav CMS")
    print("=" * 80)
    
    # Находим все markdown файлы
    md_files = list(BASE_DIR.rglob("*.md"))
    print(f"\nFound {len(md_files)} markdown files")
    
    total_downloaded = 0
    processed_files = 0
    
    # Обрабатываем каждый файл
    for md_file in md_files:
        count = process_markdown_file(md_file)
        if count > 0:
            processed_files += 1
            total_downloaded += count
    
    # Итоговая статистика
    print("\n" + "=" * 80)
    print(f"[DONE] Processed files: {processed_files}")
    print(f"[DONE] Total images: {total_downloaded}")
    print("=" * 80)

if __name__ == "__main__":
    main()
