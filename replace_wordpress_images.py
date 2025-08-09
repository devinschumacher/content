#!/usr/bin/env python3
import os
import re
from pathlib import Path
from urllib.parse import urlparse

# Configuration
CONTENT_DIR = "/Users/devin/repos/projects/content/content/post"
UPLOADS_DIR = "/Users/devin/repos/projects/content/uploads/images"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/devinschumacher/uploads/main/images"

def extract_filename_from_wp_url(url):
    """Extract just the filename from a WordPress URL"""
    # Parse the URL and get the path
    parsed = urlparse(url)
    path = parsed.path
    
    # Get the filename (last part of the path)
    filename = os.path.basename(path)
    
    # Remove any size suffixes like -1024x768 but keep the extension
    # Pattern: filename-widthxheight-optionalNumber.ext -> filename.ext
    pattern = r'^(.+?)(?:-\d+x\d+)?(?:-\d+)?(\.(?:png|jpg|jpeg|gif|webp))$'
    match = re.match(pattern, filename, re.IGNORECASE)
    
    if match:
        base_name = match.group(1)
        extension = match.group(2)
        return base_name + extension
    
    return filename

def get_available_images():
    """Get list of images available in the uploads repo"""
    if not os.path.exists(UPLOADS_DIR):
        return set()
    return set(os.listdir(UPLOADS_DIR))

def find_wordpress_urls(content):
    """Find all WordPress image URLs in content"""
    # Pattern to match WordPress uploads URLs
    patterns = [
        r'https?://devinschumacher\.com/wp-content/uploads/[^)"\s]+',
        r'https?://staging-devinschumacher\.kinsta\.cloud/wp-content/uploads/[^)"\s]+',
        r'https?://[^/]+/wp-content/uploads/[^)"\s]+'
    ]
    
    urls = []
    for pattern in patterns:
        matches = re.findall(pattern, content)
        urls.extend(matches)
    
    return urls

def replace_wordpress_urls(content, available_images):
    """Replace WordPress URLs with GitHub URLs"""
    wp_urls = find_wordpress_urls(content)
    replacements = []
    not_found = []
    
    for wp_url in wp_urls:
        # Extract filename from WordPress URL
        filename = extract_filename_from_wp_url(wp_url)
        
        # Check if we have this image
        if filename in available_images:
            github_url = f"{GITHUB_RAW_URL}/{filename}"
            content = content.replace(wp_url, github_url)
            replacements.append((wp_url, github_url))
        else:
            # Try with different extensions
            base_name = os.path.splitext(filename)[0]
            found = False
            for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
                test_filename = base_name + ext
                if test_filename in available_images:
                    github_url = f"{GITHUB_RAW_URL}/{test_filename}"
                    content = content.replace(wp_url, github_url)
                    replacements.append((wp_url, github_url))
                    found = True
                    break
            
            if not found:
                # Try with size suffix patterns
                for img in available_images:
                    if img.startswith(base_name) and any(img.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp']):
                        github_url = f"{GITHUB_RAW_URL}/{img}"
                        content = content.replace(wp_url, github_url)
                        replacements.append((wp_url, github_url))
                        found = True
                        break
            
            if not found:
                not_found.append((wp_url, filename))
    
    return content, replacements, not_found

def process_all_files():
    """Process all markdown files to replace WordPress URLs"""
    available_images = get_available_images()
    print(f"Found {len(available_images)} images in uploads repo")
    
    total_files = 0
    total_replacements = 0
    all_not_found = []
    
    for root, dirs, files in os.walk(CONTENT_DIR):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                
                with open(file_path, 'r') as f:
                    content = f.read()
                
                if 'wp-content/uploads' in content:
                    new_content, replacements, not_found = replace_wordpress_urls(content, available_images)
                    
                    if replacements:
                        with open(file_path, 'w') as f:
                            f.write(new_content)
                        
                        rel_path = os.path.relpath(file_path, CONTENT_DIR)
                        print(f"\n✓ {rel_path}: {len(replacements)} replacements")
                        for old, new in replacements[:3]:
                            old_file = os.path.basename(old)
                            new_file = os.path.basename(new)
                            print(f"  {old_file} → {new_file}")
                        if len(replacements) > 3:
                            print(f"  ... and {len(replacements) - 3} more")
                        
                        total_files += 1
                        total_replacements += len(replacements)
                    
                    all_not_found.extend(not_found)
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"✓ Updated {total_files} files")
    print(f"✓ Replaced {total_replacements} WordPress URLs")
    
    if all_not_found:
        # Deduplicate not found list
        unique_not_found = {}
        for url, filename in all_not_found:
            if filename not in unique_not_found:
                unique_not_found[filename] = url
        
        print(f"\n⚠ {len(unique_not_found)} images not found in uploads repo:")
        for filename, url in list(unique_not_found.items())[:10]:
            print(f"  - {filename}")
        if len(unique_not_found) > 10:
            print(f"  ... and {len(unique_not_found) - 10} more")
        
        # Save list of missing images
        with open('/Users/devin/repos/projects/content/missing_wordpress_images.txt', 'w') as f:
            f.write("Missing WordPress images that need to be uploaded:\n\n")
            for filename, url in unique_not_found.items():
                f.write(f"{filename}\n  Original URL: {url}\n\n")
        print(f"\nFull list saved to: missing_wordpress_images.txt")

if __name__ == "__main__":
    process_all_files()