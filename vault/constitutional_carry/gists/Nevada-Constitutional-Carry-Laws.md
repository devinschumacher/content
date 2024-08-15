import os
import re

def keep_relevant_content(content):
    print("Original content length:", len(content))
    
    # Keep only the content up to the first occurrence of either phrase
    pattern = r'(?:###\s*Gun Permit Laws by State|###\s*Search \[USA CCW Law)'
    match = re.search(pattern, content, re.IGNORECASE)
    
    if match:
        kept_content = content[:match.start()].strip()
    else:
        kept_content = content.strip()
    
    print("Kept content length:", len(kept_content))
    return kept_content

def process_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"Processing file: {input_path}")
        kept_content = keep_relevant_content(content)
        
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(kept_content)
        
        print(f"Kept content written to: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
        return False

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_count = 0
    success_count = 0
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            if process_file(input_path, output_path):
                success_count += 1
            file_count += 1
    
    print(f"\nTotal files processed: {file_count}")
    print(f"Successfully updated files: {success_count}")

# Usage
input_directory = '/Users/devin/Desktop/gun-laws/Constitutional Carry Markdown'
output_directory = '/Users/devin/Desktop/gun-laws/Constitutional Carry Cleaned'
process_directory(input_directory, output_directory)