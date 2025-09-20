import re

with open('my_log.txt', 'r') as file:
    log_text = file.read()

# 1. Ищем IP-адреса - просто "числа.числа.числа.числа"
print("1. IP-АДРЕСА:")
ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', log_text)
for ip in ip_list:
    print(f" - {ip}")

print()

# 2. Ищем даты - "2023-12-31 23:59:59"
print("2. ДАТЫ И ВРЕМЯ:")
date_list = re.findall(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', log_text)
for date in date_list:
    print(f" - {date}")

print()

# 3. Ищем БОЛЬШИЕ слова - только заглавные буквы
print("3. БОЛЬШИЕ СЛОВА:")
big_words = re.findall(r'[A-Z][A-Z]+', log_text)
for word in big_words:
    print(f" - {word}")

print()

# 4. Скрываем email - заменяем на [EMAIL PROTECTED]
print("4. ТЕКСТ БЕЗ EMAIL:")
safe_text = re.sub(r'\w+@\w+\.\w+', '[EMAIL PROTECTED]', log_text)
print(safe_text)