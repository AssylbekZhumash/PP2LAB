import shutil
import os

def copy_file(src, dst):
    if not os.path.exists(src):
        print("❌ Исходный файл не найден.")
        return
    
    shutil.copyfile(src, dst)
    print(f"✅ Файл {src} скопирован в {dst}")

copy_file("test_folder/file1.txt", "test_folder/copy_of_file1.txt")
