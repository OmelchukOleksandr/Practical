'''11.Створення програми для обчислення функції'''
x = int(input('Введіть значення x: '))

if x<=0:
    y = -2*x**2 + x + 1
else:
    y = -2*x**2 + 3

print('Значення y: ', y)
