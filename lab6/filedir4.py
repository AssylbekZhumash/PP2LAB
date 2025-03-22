import os

def count_lines(filename):
    if not os.path.exists(filename):
        print("❌ Файл не найден.")
        return
    
    with open(filename, 'r') as f:
        print(f"📄 Количество строк в {filename}: {sum(1 for line in f)}")

count_lines("test_folder/file1.txt")
