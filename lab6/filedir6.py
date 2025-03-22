import string
import os

def generate_files():
    os.makedirs("test_folder", exist_ok=True) 
    for letter in string.ascii_uppercase:
        with open(f"test_folder/{letter}.txt", 'w') as f:
            f.write(f"This is {letter}.txt")
    print("✅ 26 файлов созданы!")

generate_files()
