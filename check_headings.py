#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка семантической структуры заголовков в Markdown файлах Grav CMS
Анализирует H1-H6 на предмет правильной иерархии и множественных H1
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Конфигурация
PAGES_DIR = r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"
REPORT_FILE = "headings_report.txt"

# Статистика
issues = []
stats = {
    'files_processed': 0,
    'files_with_issues': 0,
    'multiple_h1': 0,
    'skipped_levels': 0,
    'no_h1': 0
}

def extract_frontmatter_title(content):
    """
    Извлекает title из YAML frontmatter (это считается H1)
    """
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if frontmatter_match:
        yaml_content = frontmatter_match.group(1)
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', yaml_content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
    return None

def extract_headings(content):
    """
    Извлекает все заголовки из контента (HTML и Markdown)
    Возвращает список кортежей (уровень, текст, позиция)
    """
    headings = []
    
    # HTML заголовки <h1>...</h1>
    html_pattern = r'<h([1-6])[^>]*>(.*?)</h\1>'
    for match in re.finditer(html_pattern, content, re.IGNORECASE | re.DOTALL):
        level = int(match.group(1))
        text = re.sub(r'<[^>]+>', '', match.group(2))  # Убираем внутренние теги
        text = text.strip()
        headings.append((level, text, match.start()))
    
    # Markdown заголовки # Заголовок
    md_pattern = r'^(#{1,6})\s+(.+)$'
    for match in re.finditer(md_pattern, content, re.MULTILINE):
        level = len(match.group(1))
        text = match.group(2).strip()
        headings.append((level, text, match.start()))
    
    # Сортируем по позиции
    headings.sort(key=lambda x: x[2])
    
    return headings

def check_heading_hierarchy(headings, file_path, has_frontmatter_title):
    """
    Проверяет правильность иерархии заголовков
    """
    file_issues = []
    
    # Подсчет H1
    h1_count = sum(1 for level, _, _ in headings if level == 1)
    
    # Если есть title в frontmatter, он считается как H1
    total_h1 = h1_count + (1 if has_frontmatter_title else 0)
    
    # Проверка 1: Множественные H1
    if total_h1 > 1:
        stats['multiple_h1'] += 1
        file_issues.append({
            'type': 'multiple_h1',
            'message': f'Найдено {total_h1} заголовков H1 (включая title в frontmatter)',
            'severity': 'high'
        })
    
    # Проверка 2: Отсутствие H1
    if total_h1 == 0:
        stats['no_h1'] += 1
        file_issues.append({
            'type': 'no_h1',
            'message': 'Отсутствует заголовок H1',
            'severity': 'high'
        })
    
    # Проверка 3: Пропущенные уровни (например H1 -> H3 без H2)
    prev_level = 0 if not has_frontmatter_title else 1
    
    for level, text, _ in headings:
        if level > prev_level + 1:
            stats['skipped_levels'] += 1
            file_issues.append({
                'type': 'skipped_level',
                'message': f'Пропущен уровень: H{prev_level} -> H{level} ("{text[:50]}...")',
                'severity': 'medium'
            })
        prev_level = level
    
    return file_issues

def analyze_file(file_path):
    """
    Анализирует один markdown файл
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        stats['files_processed'] += 1
        
        # Извлекаем title из frontmatter
        frontmatter_title = extract_frontmatter_title(content)
        
        # Извлекаем все заголовки
        headings = extract_headings(content)
        
        # Проверяем иерархию
        file_issues = check_heading_hierarchy(headings, file_path, bool(frontmatter_title))
        
        if file_issues:
            stats['files_with_issues'] += 1
            rel_path = os.path.relpath(file_path, PAGES_DIR)
            
            issues.append({
                'file': rel_path,
                'frontmatter_title': frontmatter_title,
                'headings': headings,
                'issues': file_issues
            })
        
    except Exception as e:
        print(f"[ОШИБКА] Анализ {file_path}: {e}")

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

def generate_report():
    """
    Генерирует отчет о проблемах
    """
    report_path = os.path.join(os.path.dirname(PAGES_DIR), REPORT_FILE)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("ОТЧЕТ О ПРОВЕРКЕ СТРУКТУРЫ ЗАГОЛОВКОВ\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Обработано файлов:           {stats['files_processed']}\n")
        f.write(f"Файлов с проблемами:         {stats['files_with_issues']}\n")
        f.write(f"Множественные H1:            {stats['multiple_h1']}\n")
        f.write(f"Отсутствие H1:               {stats['no_h1']}\n")
        f.write(f"Пропущенные уровни:          {stats['skipped_levels']}\n\n")
        
        if issues:
            f.write("=" * 80 + "\n")
            f.write("ПРОБЛЕМНЫЕ ФАЙЛЫ\n")
            f.write("=" * 80 + "\n\n")
            
            for item in issues:
                f.write("-" * 80 + "\n")
                f.write(f"📄 Файл: {item['file']}\n")
                f.write("-" * 80 + "\n")
                
                if item['frontmatter_title']:
                    f.write(f"Title (frontmatter): {item['frontmatter_title']}\n\n")
                
                f.write("Структура заголовков:\n")
                for level, text, _ in item['headings']:
                    indent = "  " * (level - 1)
                    f.write(f"{indent}H{level}: {text[:60]}\n")
                
                f.write("\nПроблемы:\n")
                for issue in item['issues']:
                    severity_icon = "🔴" if issue['severity'] == 'high' else "🟡"
                    f.write(f"{severity_icon} {issue['message']}\n")
                
                f.write("\n")
        else:
            f.write("✅ Проблем не найдено! Все заголовки имеют правильную структуру.\n")
    
    return report_path

def main():
    """
    Основная функция
    """
    print("=" * 80)
    print("[АНАЛИЗ] Структура заголовков в Grav CMS")
    print("=" * 80)
    print()
    
    if not os.path.exists(PAGES_DIR):
        print(f"[ОШИБКА] Директория не найдена: {PAGES_DIR}")
        return
    
    # Находим все markdown файлы
    print(f"[ПОИСК] Сканирование директории: {PAGES_DIR}")
    md_files = find_markdown_files(PAGES_DIR)
    print(f"[OK] Найдено {len(md_files)} markdown файлов")
    print()
    
    # Анализируем файлы
    print("[ПРОЦЕСС] Анализ файлов...")
    for file_path in md_files:
        analyze_file(file_path)
    
    print()
    print("=" * 80)
    print("[СТАТИСТИКА]")
    print("=" * 80)
    print(f"Обработано файлов:           {stats['files_processed']}")
    print(f"Файлов с проблемами:         {stats['files_with_issues']}")
    print(f"Множественные H1:            {stats['multiple_h1']}")
    print(f"Отсутствие H1:               {stats['no_h1']}")
    print(f"Пропущенные уровни:          {stats['skipped_levels']}")
    print()
    
    # Генерируем отчет
    report_path = generate_report()
    print(f"[ОТЧЕТ] Сохранен: {report_path}")
    print()
    
    # Выводим топ проблемных файлов
    if issues:
        print("[ПРОБЛЕМЫ] Топ-10 проблемных файлов:")
        print("-" * 80)
        for i, item in enumerate(issues[:10], 1):
            issue_count = len(item['issues'])
            print(f"{i}. {item['file']} ({issue_count} проблем)")
        print()
    else:
        print("[OK] Проблем не найдено!")
        print()
    
    print("[РЕКОМЕНДАЦИИ]")
    print("   - У каждой страницы должен быть ровно один H1")
    print("   - Title в frontmatter считается как H1")
    print("   - Не пропускайте уровни (H1 -> H2 -> H3, а не H1 -> H3)")
    print("   - Используйте заголовки для семантической структуры, а не стилей")

if __name__ == "__main__":
    main()
