import os
import re
from pathlib import Path

# Enhanced Bulma to Bootstrap 5 mappings
replacements = {
    # Layout - Columns
    'columns is-multiline': 'row g-3',
    'columns is-centered': 'row justify-content-center',
    'columns is-vcentered': 'row align-items-center',
    'columns is-mobile': 'row',
    'columns': 'row',
    
    # Column sizes - Mobile first
    'column is-12-mobile': 'col-12',
    'column is-6-mobile': 'col-6',
    'column is-4-mobile': 'col-4',
    'column is-3-mobile': 'col-3',
    'column is-half-mobile': 'col-6',
    
    # Column sizes - Tablet
    'column is-12-tablet': 'col-md-12',
    'column is-6-tablet': 'col-md-6',
    'column is-4-tablet': 'col-md-4',
    'column is-3-tablet': 'col-md-3',
    'column is-half-tablet': 'col-md-6',
    'column is-one-third-tablet': 'col-md-4',
    'column is-one-quarter-tablet': 'col-md-3',
    
    # Column sizes - Desktop
    'column is-12-desktop': 'col-lg-12',
    'column is-8-desktop': 'col-lg-8',
    'column is-6-desktop': 'col-lg-6',
    'column is-5-desktop': 'col-lg-5',
    'column is-4-desktop': 'col-lg-4',
    'column is-3-desktop': 'col-lg-3',
    'column is-half-desktop': 'col-lg-6',
    'column is-one-third-desktop': 'col-lg-4',
    'column is-one-quarter-desktop': 'col-lg-3',
    'column is-one-sixth-desktop': 'col-lg-2',
    
    # Generic column sizes
    'column is-12': 'col-12',
    'column is-9': 'col-9',
    'column is-8': 'col-8',
    'column is-7': 'col-7',
    'column is-6': 'col-6',
    'column is-5': 'col-5',
    'column is-4': 'col-4',
    'column is-3': 'col-3',
    'column is-2': 'col-2',
    'column is-half': 'col-6',
    'column is-one-third': 'col-4',
    'column is-one-quarter': 'col-3',
    'column is-one-sixth': 'col-2',
    'column': 'col',
    
    # Container
    'container is-widescreen': 'container-fluid',
    'container': 'container',
    
    # Hero sections -> Bootstrap equivalents
    'hero is-primary': 'bg-primary text-white',
    'hero is-info': 'bg-info text-white',
    'hero is-success': 'bg-success text-white',
    'hero is-warning': 'bg-warning text-dark',
    'hero is-danger': 'bg-danger text-white',
    'hero is-light': 'bg-light',
    'hero is-dark': 'bg-dark text-white',
    'hero-body': 'py-5',
    
    # Box -> Card
    'box': 'card',
    'card-content': 'card-body',
    'card-header-title': 'card-title',
    
    # Buttons
    'button is-primary': 'btn btn-primary',
    'button is-info': 'btn btn-info',
    'button is-success': 'btn btn-success',
    'button is-warning': 'btn btn-warning',
    'button is-danger': 'btn btn-danger',
    'button is-light': 'btn btn-light',
    'button is-dark': 'btn btn-dark',
    'button is-secondary': 'btn btn-secondary',
    'button': 'btn btn-primary',
    
    # Button modifiers
    ' is-large': ' btn-lg',
    ' is-small': ' btn-sm',
    ' is-fullwidth': ' w-100',
    ' is-outlined': ' btn-outline',
    
    # Typography - Titles
    'title is-1': 'h1 display-1',
    'title is-2': 'h2 display-2',
    'title is-3': 'h3 display-3',
    'title is-4': 'h4 display-4',
    'title is-5': 'h5',
    'title is-6': 'h6',
    'title': 'h3',
    
    # Subtitles
    'subtitle is-1': 'h2 display-1',
    'subtitle is-2': 'h2 display-2',
    'subtitle is-3': 'h3 display-3',
    'subtitle is-4': 'h4 lead',
    'subtitle is-5': 'h5 lead',
    'subtitle is-6': 'h6',
    'subtitle': 'lead',
    
    # Size utilities
    'is-size-1': 'fs-1',
    'is-size-2': 'fs-2',
    'is-size-3': 'fs-3',
    'is-size-4': 'fs-4',
    'is-size-5': 'fs-5',
    'is-size-6': 'fs-6',
    'is-size-7': 'fs-6',
    
    # Text alignment
    'has-text-centered': 'text-center',
    'has-text-left': 'text-start',
    'has-text-right': 'text-end',
    'has-text-justified': 'text-justify',
    
    # Text colors
    'has-text-white': 'text-white',
    'has-text-black': 'text-dark',
    'has-text-dark': 'text-dark',
    'has-text-primary': 'text-primary',
    'has-text-info': 'text-info',
    'has-text-success': 'text-success',
    'has-text-warning': 'text-warning',
    'has-text-danger': 'text-danger',
    'has-text-grey': 'text-muted',
    'has-text-muted': 'text-muted',
    
    # Background colors
    'has-background-primary': 'bg-primary',
    'has-background-info': 'bg-info',
    'has-background-success': 'bg-success',
    'has-background-warning': 'bg-warning',
    'has-background-danger': 'bg-danger',
    'has-background-light': 'bg-light',
    'has-background-dark': 'bg-dark',
    'has-background-white': 'bg-white',
    'has-background-grey': 'bg-secondary',
    'has-background-secondary': 'bg-secondary',
    
    # Card backgrounds
    'card-header has-background-primary': 'card-header bg-primary text-white',
    'card-header has-background-info': 'card-header bg-info text-white',
    'card-header has-background-success': 'card-header bg-success text-white',
    'card-header has-background-warning': 'card-header bg-warning text-dark',
    'card-header has-background-danger': 'card-header bg-danger text-white',
    'card-header has-background-dark': 'card-header bg-dark text-white',
    'card-header has-background-secondary': 'card-header bg-secondary text-white',
    
    # Spacing utilities (Bootstrap 5 uses 0-5 scale)
    ' mb-6': ' mb-5',
    ' mt-6': ' mt-5',
    ' pb-6': ' pb-5',
    ' pt-6': ' pt-5',
    
    # Margin/Padding direction updates (Bootstrap 5 uses start/end instead of left/right)
    ' ml-0': ' ms-0',
    ' ml-2': ' ms-2',
    ' ml-3': ' ms-3',
    ' ml-4': ' ms-4',
    ' ml-5': ' ms-5',
    ' mr-2': ' me-2',
    ' mr-3': ' me-3',
    ' mr-4': ' me-4',
    ' mr-5': ' me-5',
    
    # Flex utilities
    'is-flex': 'd-flex',
    'is-flex-direction-column': 'flex-column',
    'is-flex-direction-row': 'flex-row',
    'is-align-items-center': 'align-items-center',
    'is-justify-content-center': 'justify-content-center',
    
    # Display utilities
    'is-hidden': 'd-none',
    'is-block': 'd-block',
    'is-inline': 'd-inline',
    'is-inline-block': 'd-inline-block',
    
    # Misc utilities
    'is-rounded': 'rounded',
    'is-bold': 'fw-bold',
    'has-shadow': 'shadow',
    ' has-shadow': ' shadow',
    'is-shadowless': 'shadow-none',
    
    # Notification -> Alert
    'notification is-primary': 'alert alert-primary',
    'notification is-info': 'alert alert-info',
    'notification is-success': 'alert alert-success',
    'notification is-warning': 'alert alert-warning',
    'notification is-danger': 'alert alert-danger',
    
    # Remove Bulma-specific classes that don't need replacement
    ' is-widescreen': '',
    ' is-light': '',
    ' is-striped': '',
    ' is-bordered': '',
    ' is-hoverable': '',
    ' is-fullwidth': ' w-100',
    ' is-variable is-6': '',
    ' is-mobile is-centered': '',
    ' is-unstyled': ' list-unstyled',
    ' is-bold': ' fw-bold',
}

def convert_bulma_to_bootstrap(content):
    """Convert Bulma classes to Bootstrap 5 classes"""
    # Sort replacements by length (longest first) to avoid partial replacements
    sorted_replacements = sorted(replacements.items(), key=lambda x: len(x[0]), reverse=True)
    
    for old, new in sorted_replacements:
        content = content.replace(old, new)
    
    return content

def extract_title(content):
    """Extract title from h1 or h2 tags"""
    # Try h1 first
    match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        # Remove HTML tags from title
        title = re.sub(r'<[^>]+>', '', title)
        return title, 1
    
    # Try h2 if no h1
    match = re.search(r'<h2[^>]*>(.*?)</h2>', content, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        title = re.sub(r'<[^>]+>', '', title)
        return title, 2
    
    return 'Без названия', 0

def convert_to_grav(filepath, folder_name):
    """Convert index.txt to Grav format with Bootstrap 5"""
    try:
        # Read content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title, heading_level = extract_title(content)
        
        # Remove the h1/h2 from content
        if heading_level > 0:
            content = re.sub(f'<h{heading_level}[^>]*>.*?</h{heading_level}>', '', content, count=1, flags=re.IGNORECASE | re.DOTALL)
        
        # Convert Bulma to Bootstrap 5
        content = convert_bulma_to_bootstrap(content)
        
        # Create frontmatter
        frontmatter = f"""---
title: '{title}'
---

"""
        
        # Combine
        new_content = frontmatter + content
        
        # Write to new file
        dirpath = os.path.dirname(filepath)
        new_filepath = os.path.join(dirpath, 'default.ru.md')
        
        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, title
    except Exception as e:
        return False, str(e)

def main():
    """Main conversion function"""
    print("🚀 Начинаю конвертацию Bludit → Grav (Bootstrap 5)")
    print("=" * 60)
    
    base_path = 'user/bludit'
    success_count = 0
    error_count = 0
    errors = []
    
    # Walk through all directories
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == 'index.txt':
                filepath = os.path.join(root, file)
                folder_name = os.path.basename(root)
                
                # Convert file
                success, result = convert_to_grav(filepath, folder_name)
                
                if success:
                    success_count += 1
                    print(f"✅ {folder_name}: {result}")
                else:
                    error_count += 1
                    errors.append((folder_name, result))
                    print(f"❌ {folder_name}: {result}")
    
    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Результаты конвертации:")
    print(f"  ✅ Успешно: {success_count}")
    print(f"  ❌ Ошибок:  {error_count}")
    print(f"  📁 Всего:   {success_count + error_count}")
    
    if errors:
        print("\n⚠️  Список ошибок:")
        for folder, error in errors:
            print(f"  - {folder}: {error}")
    
    print("\n✨ Конвертация завершена!")

if __name__ == '__main__':
    main()
