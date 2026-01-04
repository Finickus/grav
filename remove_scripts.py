import os
import re
from pathlib import Path

PAGES_DIR = r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"

stats = {
    'processed': 0,
    'modified': 0,
    'jquery': 0,
    'bootstrap': 0,
    'popper': 0,
    'comments': 0,
    'jquery_scripts': 0
}

def remove_scripts_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    original = content
    stats['processed'] += 1
    
    # Remove jQuery
    jquery_pattern = r'<script\s+src=["\']https?://code\.jquery\.com/jquery-[^"\']+["\']>\s*</script>'
    jquery_count = len(re.findall(jquery_pattern, content))
    stats['jquery'] += jquery_count
    content = re.sub(jquery_pattern, '', content)
    
    # Remove Bootstrap JS
    bootstrap_pattern = r'<script\s+src=["\']https?://(cdn\.jsdelivr\.net/npm/bootstrap|stackpath\.bootstrapcdn\.com/bootstrap)/[^"\']+["\']>\s*</script>'
    bootstrap_count = len(re.findall(bootstrap_pattern, content))
    stats['bootstrap'] += bootstrap_count
    content = re.sub(bootstrap_pattern, '', content)
    
    # Remove Popper.js
    popper_pattern = r'<script\s+src=["\']https?://cdn\.jsdelivr\.net/npm/popper\.js@[^"\']+["\']>\s*</script>'
    popper_count = len(re.findall(popper_pattern, content))
    stats['popper'] += popper_count
    content = re.sub(popper_pattern, '', content)
    
    # Remove comments
    comment_patterns = [
        r'<!--\s*Подключение\s+(иконок\s+Font\s+Awesome\s+и\s+)?Bootstrap\s+JS\s*-->',
        r'<!--\s*Bootstrap\s+JS\s+и\s+зависимости\s*-->'
    ]
    for pattern in comment_patterns:
        comment_count = len(re.findall(pattern, content))
        stats['comments'] += comment_count
        content = re.sub(pattern, '', content)
    
    # Remove jQuery scripts
    jquery_script_pattern = r'(?s)<script>\s*\$\(document\)\.ready\(.*?\);\s*</script>'
    jquery_script_count = len(re.findall(jquery_script_pattern, content))
    stats['jquery_scripts'] += jquery_script_count
    content = re.sub(jquery_script_pattern, '', content)
    
    # Clean empty <p></p> tags
    content = re.sub(r'<p>\s*</p>\s*<p>\s*</p>', '', content)
    content = re.sub(r'<p>\s*</p>\s*$', '', content)
    
    if content != original:
        # Save backup
        backup_path = str(filepath) + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original)
        
        # Save modified file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        stats['modified'] += 1
        return True
    
    return False

print("\nRemoving jQuery and Bootstrap scripts...")
print("=" * 80)

pages_path = Path(PAGES_DIR)
md_files = list(pages_path.rglob('*.md'))
print(f"Found {len(md_files)} markdown files\n")

for filepath in md_files:
    if remove_scripts_from_file(filepath):
        print(f"Modified: {filepath.relative_to(pages_path)}")

print("\n" + "=" * 80)
print("STATISTICS")
print("=" * 80)
print(f"Processed: {stats['processed']} files")
print(f"Modified: {stats['modified']} files")
print(f"\nJQuery removed: {stats['jquery']}")
print(f"Bootstrap JS removed: {stats['bootstrap']}")
print(f"Popper.js removed: {stats['popper']}")
print(f"Comments removed: {stats['comments']}")
print(f"jQuery scripts removed: {stats['jquery_scripts']}")
print("=" * 80)

if stats['modified'] > 0:
    print("\nBackup files saved with .backup extension")

print("\nDone!\n")
