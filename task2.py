from math import pi
radius = 5
a = 5
print('площадь круга:-', round(pi *radius**2, 2))
print('длинна окружности:', round(pi * radius * 2, 2))
print('периметер квадрата:', a * 4)
print('площадь квадрата:' , a**2)

volume = 1.44
pages = 100
lines = 50
chars = 25
bytes_in_char = 4
print(int(volume*1024**2 // (pages * lines * chars * bytes_in_char)))

print('0' * 20 + '1' * 50 + '2' * 30)

price = float(input("цена за кб: "))
speed = int(input("скорость(в байт/сек): "))
time = float(input("за какое время скачано(в минутах): "))
volume = time * price * 60 / 1024
if volume > 500:
    cost = (volume - 500) * price
else:
    cost = 0
    print('обьем:', volume, '\nстоимость:', cost)


