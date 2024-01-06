from math import sin
from random import randint

# array = [55, 342, 12, 124, 4, 23, 43, 1, 7, 16, 23, 11, 11256, 34]
array = [randint(1, 100) for i in range(10000)]
print(array)


# Сортировка массива, метод пузырька
def bubble_sorted(): 
    swapped = True
    last_index = len(array) - 1
    while swapped is True:
        swapped = False
        for item_index in range(last_index):
            if array[item_index] > array[item_index + 1]:
                array[item_index], array[item_index + 1] = array[item_index + 1], array[item_index]
                swapped = True
                item_index += 1
    print(array)


if __name__ == '__main__':
    bubble_sorted()
