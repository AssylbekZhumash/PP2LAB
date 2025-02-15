from datetime import datetime, timedelta

# 1. Вычесть 5 дней из текущей даты
current_date = datetime.now()
date_minus_5 = current_date - timedelta(days=5)
print("Дата минус 5 дней:", date_minus_5.strftime("%Y-%m-%d"))

# 2. Напечатать вчера, сегодня, завтра
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Вчера:", yesterday.strftime("%Y-%m-%d"))
print("Сегодня:", current_date.strftime("%Y-%m-%d"))
print("Завтра:", tomorrow.strftime("%Y-%m-%d"))

# 3. Убрать микросекунды из datetime
datetime_without_microseconds = current_date.replace(microsecond=0)
print("Дата без микросекунд:", datetime_without_microseconds)

# 4. Разница между двумя датами в секундах
date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 14, 30, 0)
difference_in_seconds = int((date2 - date1).total_seconds())
print("Разница в секундах:", difference_in_seconds)
