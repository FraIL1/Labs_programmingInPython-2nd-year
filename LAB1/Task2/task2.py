import re

with open('my_log.txt', 'r') as file:
    log_text = file.read()


print("1. IP-АДРЕСА:")
ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', log_text)
for ip in ip_list:
    print(f" - {ip}")

print()

print("2. ДАТЫ И ВРЕМЯ:")
date_list = re.findall(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', log_text)
for date in date_list:
    print(f" - {date}")

print()


print("3. БОЛЬШИЕ СЛОВА:")
big_words = re.findall(r'[A-Z][A-Z]+', log_text)
for word in big_words:
    print(f" - {word}")

print()


print("4. ТЕКСТ БЕЗ EMAIL:")
safe_text = re.sub(r'\w+@\w+\.\w+', '[EMAIL PROTECTED]', log_text)
print(safe_text)
