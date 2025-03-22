import os

def list_contents(path):
    if not os.path.exists(path):
        print("❌ Указанный путь не существует.")
        return

    all_items = os.listdir(path)
    files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
    directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]

    print("📂 Директории:", directories)
    print("📄 Файлы:", files)
    print("📋 Все элементы:", all_items)

list_contents("test_folder")  
