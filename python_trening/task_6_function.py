# определяем функцию
def add(x, y):
    return x+y
# вызываем функцию
print(add(1, 2))

#вызываем функцию с другими аргументами
print(add('I a', 'm tester'))

def add (a=(1, 2, 3, 4)):
    return a[1]
print(add())
def add(radius, pi=3.14159):
    return pi * radius * radius
print (add(2))