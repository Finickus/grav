#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для исправления путей к изображениям в Grav CMS
Добавляет правильные относительные пути для страниц
"""

import os
import sys
import re
from pathlib import Path

# Настройка вывода для Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Конфигурация
BASE_DIR = Path(r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages")

def get_page_url_path(page_dir):
    """
    Получает URL путь страницы из файловой структуры
    Например: 02.uslugi/02.remont-kotlov -> /uslugi/remont-kotlov/
    """
    relative_path = page_dir.relative_to(BASE_DIR)
    parts = relative_path.parts
    
    # Убираем числовые префиксы из названий папок
    clean_parts = []
    for part in parts:
        # Удаляем префикс вида "01." или "02."
        clean_part = re.sub(r'^\d+\.', '', part)
        clean_parts.append(clean_part)
    
    return '/' + '/'.join(clean_parts) + '/' if clean_parts else '/'

def fix_image_paths_in_file(md_file_path):
    """
    Исправляет пути к изображениям в markdown файле
    """
    print(f"\n[FILE] Processing: {md_file_path.relative_to(BASE_DIR)}")
    
    try:
        # Читаем содержимое файла
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Директория страницы
        page_dir = md_file_path.parent
        
        # Получаем URL путь страницы
        page_url = get_page_url_path(page_dir)
        print(f"  Page URL: {page_url}")
        
        # Находим все изображения в той же директории
        image_files = []
        for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.svg', '*.webp']:
            image_files.extend(page_dir.glob(ext))
        
        if not image_files:
            print("  No local images found")
            return 0
        
        print(f"  Found {len(image_files)} local images")
        
        # Обновленное содержимое
        updated_content = content
        changes_made = 0
        
        # Для каждого изображения в директории
        for img_file in image_files:
            img_name = img_file.name
            
            # Паттерны для поиска
            # 1. HTML img tags: src="filename.jpg"
            # 2. HTML img tags: src='filename.jpg'
            patterns = [
                (f'src="{img_name}"', f'src="{page_url}{img_name}"'),
                (f"src='{img_name}'", f"src='{page_url}{img_name}'"),
            ]
            
            for old_pattern, new_pattern in patterns:
                if old_pattern in updated_content:
                    updated_content = updated_content.replace(old_pattern, new_pattern)
                    changes_made += 1
                    print(f"    Fixed: {img_name} -> {page_url}{img_name}")
        
        # Сохраняем обновленный файл, если были изменения
        if updated_content != content:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  [OK] File updated: {changes_made} paths fixed")
            return changes_made
        else:
            print("  No changes needed")
            return 0
        
    except Exception as e:
        print(f"  [ERROR] Failed to process file: {e}")
        return 0

def main():
    """
    Главная функция
    """
    print("=" * 80)
    print("Fixing image paths for Grav CMS")
    print("=" * 80)
    
    # Находим все markdown файлы
    md_files = list(BASE_DIR.rglob("*.md"))
    print(f"\nFound {len(md_files)} markdown files")
    
    total_fixed = 0
    processed_files = 0
    
    # Обрабатываем каждый файл
    for md_file in md_files:
        count = fix_image_paths_in_file(md_file)
        if count > 0:
            processed_files += 1
            total_fixed += count
    
    # Итоговая статистика
    print("\n" + "=" * 80)
    print(f"[DONE] Processed files: {processed_files}")
    print(f"[DONE] Total paths fixed: {total_fixed}")
    print("=" * 80)

if __name__ == "__main__":
    main()
