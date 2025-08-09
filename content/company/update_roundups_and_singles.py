#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Configuration
ROUNDUPS_DIR = "/Users/devin/repos/projects/content/content/company/roundups"
SINGLES_DIR = "/Users/devin/repos/projects/content/content/company/singles"
IMAGES_SOURCE = "/Users/devin/repos/projects/content/content/post/images"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/devinschumacher/uploads/main/images"
OUTPUT_DIR = "/Users/devin/repos/projects/content/content/company/images_to_upload"

def update_date_format(content):
    """Convert date from YYYY-MM-DD to ISO 8601 format"""
    # Match date: "YYYY-MM-DD" format
    pattern = r'^date: "(\d{4}-\d{2}-\d{2})"$'
    replacement = r'date: "\1T12:00:00.000Z"'
    return re.sub(pattern, replacement, content, flags=re.MULTILINE)

def extract_image_references(content):
    """Extract all image references from markdown content"""
    # Find all markdown image references: ![alt](path) and [![alt](path)](link)
    pattern = r'!\[.*?\]\((.*?)\)'
    matches = re.findall(pattern, content)
    
    # Extract just the image filenames from /images/ paths
    images = []
    for match in matches:
        if match.startswith('/images/'):
            filename = match.replace('/images/', '')
            images.append(filename)
    
    return images

def update_image_urls(content):
    """Replace local image paths with GitHub URLs"""
    # Pattern to match /images/filename
    pattern = r'/images/([^)]+)'
    
    def replace_func(match):
        filename = match.group(1)
        return f'{GITHUB_RAW_URL}/{filename}'
    
    return re.sub(pattern, replace_func, content)

def process_directory(directory, dir_name):
    """Process all markdown files in a directory"""
    print(f"\n{'='*60}")
    print(f"Processing {dir_name}")
    print(f"{'='*60}")
    
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return set()
    
    all_images = set()
    updated_files = 0
    
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Extract images before updating
            images = extract_image_references(content)
            all_images.update(images)
            
            # Update date format
            new_content = update_date_format(content)
            
            # Update image URLs
            new_content = update_image_urls(new_content)
            
            # Write back if changed
            if new_content != content:
                with open(file_path, 'w') as f:
                    f.write(new_content)
                updated_files += 1
                print(f"  ✓ Updated: {filename}")
    
    print(f"\nUpdated {updated_files} files in {dir_name}")
    return all_images

def copy_missing_images(all_images):
    """Copy images that aren't already in the uploads repo"""
    print(f"\n{'='*60}")
    print(f"Preparing images for upload")
    print(f"{'='*60}")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Check existing images in uploads repo
    uploads_images_dir = "/Users/devin/repos/projects/content/uploads/images"
    existing_in_uploads = set()
    if os.path.exists(uploads_images_dir):
        existing_in_uploads = set(os.listdir(uploads_images_dir))
    
    copied = 0
    already_uploaded = 0
    missing = []
    
    for img in sorted(all_images):
        if img in existing_in_uploads:
            already_uploaded += 1
            continue
            
        source_path = os.path.join(IMAGES_SOURCE, img)
        dest_path = os.path.join(OUTPUT_DIR, img)
        
        if os.path.exists(source_path):
            import shutil
            shutil.copy2(source_path, dest_path)
            copied += 1
            if copied <= 5:
                print(f"  Copied: {img}")
        else:
            missing.append(img)
    
    if copied > 5:
        print(f"  ... and {copied - 5} more files")
    
    print(f"\n📊 Summary:")
    print(f"  ✓ {already_uploaded} images already in uploads repo")
    print(f"  ✓ {copied} new images copied to staging")
    if missing:
        print(f"  ⚠ {len(missing)} images not found locally")
    
    return copied

def main():
    # Process both directories
    roundups_images = process_directory(ROUNDUPS_DIR, "company/roundups")
    singles_images = process_directory(SINGLES_DIR, "company/singles")
    
    # Combine all unique images
    all_images = roundups_images | singles_images
    print(f"\n📸 Found {len(all_images)} unique images total")
    
    # Copy missing images
    new_images_count = copy_missing_images(all_images)
    
    if new_images_count > 0:
        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("="*60)
        print(f"1. {new_images_count} new images ready in: {OUTPUT_DIR}")
        print("2. Copy them to the uploads repo and push:")
        print("   cp /Users/devin/repos/projects/content/content/company/images_to_upload/* \\")
        print("      /Users/devin/repos/projects/content/uploads/images/")
        print("   cd /Users/devin/repos/projects/content/uploads")
        print("   git add images/")
        print("   git commit -m 'Add company roundups and singles images'")
        print("   git push")
    else:
        print("\n✅ All images are already uploaded! No new images to add.")

if __name__ == "__main__":
    main()