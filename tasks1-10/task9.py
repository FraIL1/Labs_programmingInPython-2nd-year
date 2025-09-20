import random

list1 = [random.randint(-10, 10) for _ in range(15)]

list2 = [x for x in list1 if x > 0]

list3 = [x**2 for x in list1]

print("Исходный список: ", list1)
print("Положительные числа: ", list2)
print("Квадраты чисел: ", list3)