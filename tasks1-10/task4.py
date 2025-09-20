start = int(input())
end = int(input())

numbers = []
for i in range(start, end + 1):
    if i % 2 == 0:
        numbers.append(i)

if numbers:
    print(*numbers)
else:
    print("В этом диапазоне нет чётных чисел.")