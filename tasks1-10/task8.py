text = input()

result = ""
for char in text:
    if 'a' <= char <= 'z':
        new_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        result += new_char
    elif 'A' <= char <= 'Z':
        new_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        result += new_char
    else:
        result += char

print(result)