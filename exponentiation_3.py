number_last = int(input('Введите целое число: '))
number_first = 1
total = 1
if number_first == number_last:
    print(total)
else:
    while number_first < number_last:
        total += (number_first ** 3)
        number_first += 1
    print(total)
