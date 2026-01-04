#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление alt атрибутов к изображениям в Markdown файлах Grav CMS
Автоматически находит <img> теги без alt и добавляет осмысленные описания
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# Конфигурация
PAGES_DIR = r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"
BACKUP_EXTENSION = ".bak"
LOG_FILE = "alt_attributes_report.txt"

# Статистика
stats = {
    'files_processed': 0,
    'files_modified': 0,
    'images_found': 0,
    'images_without_alt': 0,
    'alt_added': 0
}

def clean_filename_for_alt(filename):
    """
    Преобразует имя файла в читаемый alt текст
    Пример: 'screenshot_38(1).jpg' -> 'Screenshot 38 1'
    """
    # Убираем расширение
    name = os.path.splitext(filename)[0]
    
    # Заменяем разделители на пробелы
    name = re.sub(r'[-_]', ' ', name)
    
    # Убираем скобки и другие спецсимволы
    name = re.sub(r'[()[\]{}]', ' ', name)
    
    # Убираем множественные пробелы
    name = re.sub(r'\s+', ' ', name)
    
    # Капитализация первой буквы
    name = name.strip().capitalize()
    
    return name

def extract_context_from_heading(content, img_position):
    """
    Извлекает контекст из ближайшего заголовка перед изображением
    """
    # Берем текст до изображения
    text_before = content[:img_position]
    
    # Ищем последний заголовок (h1-h6 или markdown #)
    html_heading = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', text_before, re.IGNORECASE | re.DOTALL)
    md_heading = re.findall(r'^#{1,6}\s+(.+)$', text_before, re.MULTILINE)
    
    if html_heading:
        # Убираем HTML теги из заголовка
        heading = re.sub(r'<[^>]+>', '', html_heading[-1])
        return heading.strip()[:100]  # Максимум 100 символов
    elif md_heading:
        return md_heading[-1].strip()[:100]
    
    return None

def generate_alt_text(img_tag, src, content, img_position):
    """
    Генерирует alt текст на основе различных источников
    Приоритет:
    1. Контекст из заголовка
    2. Имя файла
    3. Родительская папка
    """
    # Извлекаем имя файла
    filename = os.path.basename(src)
    
    # Специальные случаи
    if 'logo' in filename.lower():
        brand = clean_filename_for_alt(filename).replace('Logo', '').strip()
        return f"{brand} логотип" if brand else "Логотип"
    
    if any(word in filename.lower() for word in ['schema', 'scheme', 'diagram']):
        # Пытаемся извлечь номер схемы
        number_match = re.search(r'\d+', filename)
        if number_match:
            return f"Схема {number_match.group()}"
        return "Схема"
    
    if any(word in filename.lower() for word in ['screenshot', 'скриншот']):
        # Пытаемся использовать контекст
        context = extract_context_from_heading(content, img_position)
        if context:
            return context
    
    # Проверяем контекст для общих изображений
    context = extract_context_from_heading(content, img_position)
    if context and len(context) > 10:
        return context
    
    # Используем очищенное имя файла
    alt_from_filename = clean_filename_for_alt(filename)
    if alt_from_filename and len(alt_from_filename) > 3:
        return alt_from_filename
    
    # Fallback
    return "Изображение"

def process_img_tag(match, content, file_path):
    """
    Обрабатывает один <img> тег
    """
    img_tag = match.group(0)
    img_position = match.start()
    
    stats['images_found'] += 1
    
    # Проверяем наличие alt атрибута
    if re.search(r'\salt=', img_tag, re.IGNORECASE):
        return img_tag  # Alt уже есть
    
    stats['images_without_alt'] += 1
    
    # Извлекаем src
    src_match = re.search(r'src=["\'](.*?)["\']', img_tag, re.IGNORECASE)
    if not src_match:
        return img_tag  # Не можем найти src
    
    src = src_match.group(1)
    
    # Генерируем alt текст
    alt_text = generate_alt_text(img_tag, src, content, img_position)
    
    # Вставляем alt после src
    new_img_tag = re.sub(
        r'(src=["\'][^"\']*["\'])',
        r'\1 alt="' + alt_text + '"',
        img_tag,
        count=1
    )
    
    stats['alt_added'] += 1
    return new_img_tag

def process_markdown_file(file_path):
    """
    Обрабатывает один markdown файл
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        stats['files_processed'] += 1
        
        # Находим все <img> теги
        img_pattern = r'<img[^>]*>'
        
        # Обрабатываем каждое изображение
        def replacer(match):
            return process_img_tag(match, content, file_path)
        
        new_content = re.sub(img_pattern, replacer, content, flags=re.IGNORECASE)
        
        # Если были изменения
        if new_content != original_content:
            # Создаем backup
            backup_path = str(file_path) + BACKUP_EXTENSION
            shutil.copy2(file_path, backup_path)
            
            # Записываем изменения
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            stats['files_modified'] += 1
            return True
        
        return False
        
    except Exception as e:
        print(f"[ОШИБКА] Обработка {file_path}: {e}")
        return False

def find_markdown_files(directory):
    """
    Рекурсивно находит все .md файлы
    """
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def main():
    """
    Основная функция
    """
    print("=" * 70)
    print("[ALT] Добавление alt атрибутов к изображениям в Grav CMS")
    print("=" * 70)
    print()
    
    if not os.path.exists(PAGES_DIR):
        print(f"[ОШИБКА] Директория не найдена: {PAGES_DIR}")
        return
    
    # Находим все markdown файлы
    print(f"[ПОИСК] Сканирование директории: {PAGES_DIR}")
    md_files = find_markdown_files(PAGES_DIR)
    print(f"[OK] Найдено {len(md_files)} markdown файлов")
    print()
    
    # Обрабатываем файлы
    print("[ПРОЦЕСС] Обработка файлов...")
    modified_files = []
    
    for i, file_path in enumerate(md_files, 1):
        if process_markdown_file(file_path):
            modified_files.append(file_path)
            rel_path = os.path.relpath(file_path, PAGES_DIR)
            print(f"[+] [{i}/{len(md_files)}] {rel_path}")
    
    print()
    print("=" * 70)
    print("[СТАТИСТИКА]")
    print("=" * 70)
    print(f"Обработано файлов:           {stats['files_processed']}")
    print(f"Изменено файлов:             {stats['files_modified']}")
    print(f"Найдено изображений:         {stats['images_found']}")
    print(f"Без alt атрибута:            {stats['images_without_alt']}")
    print(f"Добавлено alt атрибутов:     {stats['alt_added']}")
    print()
    
    # Создаем отчет
    report_path = os.path.join(os.path.dirname(PAGES_DIR), LOG_FILE)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"Отчет о добавлении alt атрибутов\n")
        f.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"=" * 70 + "\n\n")
        f.write(f"Обработано файлов: {stats['files_processed']}\n")
        f.write(f"Изменено файлов: {stats['files_modified']}\n")
        f.write(f"Найдено изображений: {stats['images_found']}\n")
        f.write(f"Без alt атрибута: {stats['images_without_alt']}\n")
        f.write(f"Добавлено alt атрибутов: {stats['alt_added']}\n\n")
        
        if modified_files:
            f.write("\nИзмененные файлы:\n")
            f.write("-" * 70 + "\n")
            for file_path in modified_files:
                rel_path = os.path.relpath(file_path, PAGES_DIR)
                f.write(f"{rel_path}\n")
    
    print(f"[ОТЧЕТ] Сохранен: {report_path}")
    print()
    print("[OK] Готово!")
    print()
    print("[ИНФО] Примечания:")
    print("   - Создан backup каждого измененного файла (.bak)")
    print("   - Проверьте несколько страниц вручную")
    print("   - Для отката используйте .bak файлы")

if __name__ == "__main__":
    main()
