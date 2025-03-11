import os
import zipfile
from tqdm import tqdm

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return extract_to

def find_and_replace(directory, old_word, new_word):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if old_word in content:
                    content = content.replace(old_word, new_word)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
            except Exception:
                pass

def main():
    print("==================================")
    print("  🔥 Made by HACKER TF 🔥  ")
    print("==================================\n")

    zip_path = input("Enter ZIP file path: ")
    if not os.path.exists(zip_path):
        print("❌ File not found!")
        return
    
    extract_to = "extracted_files"
    extract_zip(zip_path, extract_to)
    
    old_word = input("Enter the word to find: ")
    new_word = input("Enter the new word: ")
    
    print("\n🔄 Replacing text, please wait...")
    find_and_replace(extract_to, old_word, new_word)
    
    print("\n✅ All occurrences replaced successfully!")

if __name__ == "__main__":
    main()
