import os
import re

def convert_to_grav(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find title in <h1> tags
        match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            # Remove HTML tags from title if any
            title = re.sub(r'<[^>]+>', '', title)
        else:
            title = 'Без названия'  # Default title

        # Remove the h1 from content
        content = re.sub(r'<h1[^>]*>.*?</h1>', '', content, flags=re.IGNORECASE | re.DOTALL)

        # Create frontmatter
        frontmatter = f"""---
title: '{title}'
---
"""

        # New content
        new_content = frontmatter + content

        # Write to new file default.ru.md
        dirpath = os.path.dirname(filepath)
        new_filepath = os.path.join(dirpath, 'default.ru.md')
        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Converted {filepath} to {new_filepath}")
    except Exception as e:
        print(f"Error converting {filepath}: {e}")

# Walk the directory
for root, dirs, files in os.walk('user/bludit'):
    for file in files:
        if file == 'index.txt':
            filepath = os.path.join(root, file)
            convert_to_grav(filepath)

print("All files converted to Grav format.")
