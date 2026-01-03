import os
import hashlib
from pathlib import Path
from collections import defaultdict

def get_file_hash(filepath):
    """Calculate MD5 hash of file content"""
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def find_all_pages(pages_dir):
    """Find all markdown files in pages directory"""
    pages = []
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                pages.append(filepath)
    return pages

def analyze_duplicates(pages_dir):
    """Find duplicate pages based on content hash"""
    print("Scanning pages for duplicates...")
    
    all_pages = find_all_pages(pages_dir)
    print(f"Found {len(all_pages)} total pages")
    
    # Group files by hash
    hash_to_files = defaultdict(list)
    
    for page in all_pages:
        file_hash = get_file_hash(page)
        if file_hash:
            hash_to_files[file_hash].append(page)
    
    # Find duplicates
    duplicates = {h: files for h, files in hash_to_files.items() if len(files) > 1}
    
    print(f"\nFound {len(duplicates)} groups of duplicates")
    print("=" * 80)
    
    blog_to_delete = []
    
    for hash_val, files in duplicates.items():
        print(f"\nDuplicate group ({len(files)} files):")
        
        blog_files = []
        other_files = []
        
        for f in files:
            rel_path = os.path.relpath(f, pages_dir)
            if '\\07.blog\\' in f or '/07.blog/' in f:
                blog_files.append(f)
                print(f"  [BLOG] {rel_path}")
            else:
                other_files.append(f)
                print(f"  [OTHER] {rel_path}")
        
        # If there are duplicates with at least one in blog and one outside blog
        if blog_files and other_files:
            blog_to_delete.extend(blog_files)
            print(f"  → Will delete {len(blog_files)} blog file(s)")
    
    return blog_to_delete

def delete_files(files_to_delete, dry_run=True):
    """Delete files (or just print what would be deleted)"""
    if dry_run:
        print("\n" + "=" * 80)
        print("DRY RUN - Files that would be deleted:")
        print("=" * 80)
        for f in files_to_delete:
            print(f"  - {f}")
        print(f"\nTotal: {len(files_to_delete)} files")
    else:
        print("\n" + "=" * 80)
        print("DELETING FILES:")
        print("=" * 80)
        for f in files_to_delete:
            try:
                os.remove(f)
                print(f"  ✓ Deleted: {f}")
            except Exception as e:
                print(f"  ✗ Error deleting {f}: {e}")

if __name__ == "__main__":
    pages_dir = r"c:\Users\finic_rnd8rqs\OneDrive\Документы\GitHub\grav\user\pages"
    
    # First run analysis
    blog_to_delete = analyze_duplicates(pages_dir)
    
    # Show what would be deleted
    delete_files(blog_to_delete, dry_run=True)
    
    # Uncomment the line below to actually delete files
    # delete_files(blog_to_delete, dry_run=False)
