import json
import os

# Определяем путь к файлу
file_path = r"C:\Users\Асыл\Desktop\lab4\sample-data.json"

# Проверяем, существует ли файл
if not os.path.exists(file_path):
    print(f"Ошибка: Файл {file_path} не найден!")
    exit()

# Открываем JSON-файл и загружаем данные
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Speed':10} {'MTU':10}")
print("-" * 80)

# Извлекаем интерфейсы и их параметры
for item in data.get("imdata", []):
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "unknown")
    print(f"{dn:50} {speed:10} {mtu:10}")
