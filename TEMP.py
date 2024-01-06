def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    count = 0
    if len(list_set_1) == len(list_set_2):
        for item in list_set_1:
            if item in list_set_2:
                count += 1
        if count == len(list_set_1):
            return 'Наборы равны.'
        else:
            return 'Супермножество не обнаружено.'
    elif len(list_set_1) > len(list_set_2):
        for item in list_set_2:
            if item in list_set_1:
                count += 1
        if count == len(list_set_2):
            return f'Набор {list_set_1} - супермножество.'
        else:
            return 'Супермножество не обнаружено.'
    elif len(list_set_1) < len(list_set_2):
        for item in list_set_1:
            if item in list_set_2:
                count += 1
        if count == len(list_set_1):
            return f'Набор {list_set_2} - супермножество.'
        else:
            return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
