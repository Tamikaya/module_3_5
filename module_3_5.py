def get_multiplied_digits(number):
    str_number = str(number)#запишите строковое представление(str) числа number
    if len(str_number) > 1:#Если длина str_number больше 1
        first = int(str_number[0])#тогда вернуть оставшуюся цифру first.

 # умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(4020301)
print(result2)