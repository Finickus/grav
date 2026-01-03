import os
import re

root_path = r"user\pages"
files_processed = 0

print("Starting font-family removal process...")
print(f"Root path: {root_path}")

# Get all .md and .txt files
files = []
for dirpath, dirnames, filenames in os.walk(root_path):
    for filename in filenames:
        if filename.endswith('.md') or filename.endswith('.txt'):
            files.append(os.path.join(dirpath, filename))

print(f"Found {len(files)} files to process")

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove font-family with various patterns
    # Pattern 1: font-family: ...; (with semicolon after)
    content = re.sub(r'font-family:\s*[^;]+;\s*', '', content)
    
    # Pattern 2: ; font-family: ... (at end before quote)
    content = re.sub(r';\s*font-family:\s*[^;\'"]+(?=[\'"])', '', content)
    
    # Pattern 3: font-family: ... (at beginning or standalone)  
    content = re.sub(r'\s*font-family:\s*[^;\'"]+(?=[\'"])', '', content)
    
    # Clean up double semicolons
    content = re.sub(r';\s*;', ';', content)
    
    # Clean up style=" ; or style=' ;
    content = re.sub(r'style=(["\'])\s*;', r'style=\1', content)
    
    # Clean up ; before closing quote
    content = re.sub(r';\s*(["\'])', r'\1', content)
    
    # Remove empty style attributes
    content = re.sub(r'\s+style=(["\'])\1', ' ', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        files_processed += 1
        print(f"✓ Processed: {os.path.basename(file_path)}")

print(f"\nSummary:")
print(f"Files processed: {files_processed}")
print(f"Total files scanned: {len(files)}")
