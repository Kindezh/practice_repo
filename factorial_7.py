n = int(input('Введите натуральное число: '))
s = 1
for i in range(1, n + 1, 1):
    s *= i
print(s)
