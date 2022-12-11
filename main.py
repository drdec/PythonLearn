import random

def sum_of_odd_elements(list):
    x = len(list)
    x1 = 0
    sum = 0

    while x1 != x:
        if x1 % 2 != 0:
            sum += list[x1]
        x1 += 1

    return sum

def sum_of_line_elements(list):
    size = len(list)
    sum = 0
    for i in range(size):
        sum += list[i]

    return sum

def select_sort(A):
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]
    return A


#ЗАДАНИЕ 1
#1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print("Задание 1")

print('Введите количество элементов')

n = int(input())

list = []

while n != 0:
    print(f"Осталось {n} элементов")
    print("Введите x")
    x = int(input())
    list.append(x)
    n -= 1

print(f"Сумма элементов = {sum_of_odd_elements(list)}")



#2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
#И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
#ЗАДАНИЕ 2

print()
print("Задание 2")
print()

print("Введите A")
a = int(input())

print("Введите B")
b = int(input())

mas = []

for i in range(a):
    mas.append([0] * b)

for i in range(a):
    for j in range(b):
        mas[i][j] = random.randint(0, 20)
print("Сформированный двумерный массив")


for i in range(a):
    for j in range(b):
        print(mas[i][j], end=" ")
    print()

for i in range(a):
    sum = sum_of_line_elements(mas[i])
    print(f"Сумма первой строки равна = {sum}")


#Задание 3
#3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
print("Задание 3")

mas = [0] * 30

for i in range(len(mas)):
    mas[i] = random.randint(0, 40)

print("Наша изначальный массив ")
print(mas)

mas = select_sort(mas)

print("Массив после сортировки")
print(mas)








