#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для исправления оставшихся путей к изображениям
Обрабатывает файлы с пробелами и специальными символами в именах
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
    """Получает URL путь страницы"""
    relative_path = page_dir.relative_to(BASE_DIR)
    parts = relative_path.parts
    clean_parts = []
    for part in parts:
        clean_part = re.sub(r'^\d+\.', '', part)
        clean_parts.append(clean_part)
    return '/' + '/'.join(clean_parts) + '/' if clean_parts else '/'

def fix_remaining_paths(md_file_path):
    """Исправляет оставшиеся пути к изображениям"""
    print(f"\n[FILE] Processing: {md_file_path.relative_to(BASE_DIR)}")
    
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        page_dir = md_file_path.parent
        page_url = get_page_url_path(page_dir)
        
        # Находим все изображения в папке (включая с пробелами и спецсимволами)
        image_files = []
        for ext in ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.svg', '*.webp']:
            image_files.extend(page_dir.glob(ext))
        
        # Также ищем файлы с заглавными расширениями
        for ext in ['*.JPG', '*.JPEG', '*.PNG', '*.GIF', '*.SVG', '*.WEBP']:
            image_files.extend(page_dir.glob(ext))
        
        if not image_files:
            print("  No local images found")
            return 0
        
        print(f"  Found {len(image_files)} local images")
        print(f"  Page URL: {page_url}")
        
        updated_content = content
        changes_made = 0
        
        # Паттерн для поиска относительных путей (без слэша в начале)
        for img_file in image_files:
            img_name = img_file.name
            
            # Ищем различные варианты
            patterns = [
                # Двойные кавычки
                (f'src="{img_name}"', f'src="{page_url}{img_name}"'),
                # Одинарные кавычки
                (f"src='{img_name}'", f"src='{page_url}{img_name}'"),
                # href для ссылок
                (f'href="{img_name}"', f'href="{page_url}{img_name}"'),
                (f"href='{img_name}'", f"href='{page_url}{img_name}'"),
            ]
            
            for old_pattern, new_pattern in patterns:
                if old_pattern in updated_content:
                    updated_content = updated_content.replace(old_pattern, new_pattern)
                    changes_made += 1
                    print(f"    Fixed: {img_name}")
        
        if updated_content != content:
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  [OK] File updated: {changes_made} paths fixed")
            return changes_made
        else:
            print("  No changes needed")
            return 0
        
    except Exception as e:
        print(f"  [ERROR] Failed: {e}")
        return 0

def main():
    print("=" * 80)
    print("Fixing remaining image paths (with special characters and spaces)")
    print("=" * 80)
    
    # Получаем список проблемных файлов из grep результатов
    problem_files = [
        "09.zapchasti/remont-elektro-kotlov/default.md",
        "09.zapchasti/mora/zapchasti-dlya-elektrokotlov-mora/default.md",
        "09.zapchasti/electrolux/zapchasti-electrolux-gwh-250-275/default.md",
        "08.kody-oshibok/mora/kody-oshibok-kotla-mora/default.md",
        "07.blog/gazovaja-kolonka-bosch/default.md",
        "07.blog/kakie-priznaki-ukazyvayut-na-neobkhodimost-zameny-moego-kotla/default.md",
        "07.blog/membrana-vodjanogo-bloka-neva-4510-4511-4513/default.md",
        "07.blog/opisanie-kotla-therm-14-cln-2015g-vypuska/default.md",
        "07.blog/opisanie-kotla-therm-pro-14-xa-2015g-vypuska/default.md",
        "07.blog/remont-ehlektro-kotlov-kospel/default.md",
        "07.blog/therm-pro-14-tx-a-2020г/default.md",
        "07.blog/zapchasti-thermona/default.md",
        "07.blog/zapchasti-kotla-therm-20-tcxa-2015g/default.md",
        "07.blog/zapchasti-kotla-therm-20-cxea-2015g/default.md",
        "07.blog/zapchasti-ehlektroljuks-285/default.md",
        "07.blog/zapchasti-dlya-elektrolyuks-gwh-275-rn/default.md",
        "07.blog/zapchasti-dlja-kotla-therm-pro-14-txa-2015g-vypuska/default.md",
        "07.blog/zapchasti-dlja-gazovyx-kolonok-neva/default.md",
        "07.blog/zapchasti-dlja-ehlektrokotlov-mora/default.md",
        "07.blog/zapchast-buderus/default.md",
        "07.blog/therm-20-tcxea-2015g/default.md",
        "07.blog/therm-32-cln-2015g/default.md",
        "07.blog/therm-20-tlxzea-2015/default.md",
        "07.blog/uslugi/default.md",
    ]
    
    total_fixed = 0
    processed_files = 0
    
    for file_path in problem_files:
        full_path = BASE_DIR / file_path
        if full_path.exists():
            count = fix_remaining_paths(full_path)
            if count > 0:
                processed_files += 1
                total_fixed += count
        else:
            print(f"\n[SKIP] File not found: {file_path}")
    
    print("\n" + "=" * 80)
    print(f"[DONE] Processed files: {processed_files}")
    print(f"[DONE] Total paths fixed: {total_fixed}")
    print("=" * 80)

if __name__ == "__main__":
    main()
