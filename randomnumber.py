# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random
def zadachz1():
    number = list(random.randint(1,10) for _ in range(random.randint(5,9)))
    result = list(filter(lambda x: x > 5,number))
    print(f'Случайный список:{number}')
    print(f'Элементы больше 5 из списка: {result}')
# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
def zadacha2():
    number = list(random.randint(1,10) for _ in range(random.randint(5,12)))
    print(f'список случайных чисел: {number}')
    index = random.randint(0,len(number)-1)
    result = [number[index]]

    while index < len(number):
        index = random.randint(index,len(number)-1)
        if index!= len(number) and number[index]> result[-1]:
            result.append(number[index])
        break

    print(f'Cлучайная восрастающая последовательность:{result}')

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]
def zadacha3():
    number = list(random.randint(1,10) for _ in range(random.randint(7,10)))

    print(f'список случайных чисел: {number}')
    # result = list(filter(lambda x: number.count(x) > 1, number))
    # # print(f'{result}')

    result = list(map(lambda x: number.count(x) > 1, number))
    print(f'Количество повторений в списке {result.count(True)}')
    numbers = set(number)
    print(f'Список уникальных элементов{numbers}')
# zadachz1()
# zadacha2()
zadacha3()