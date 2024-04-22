price = float(input("цена за кб: "))
speed = int(input("скорость(в байт/сек): "))
time = float(input("за какое время скачано(в минутах): "))
volume = time * price * 60 / 1024
if volume > 500:
    cost = (volume - 500) * price
else:
    cost = 0
    print('обьем:', volume, '\nстоимость:', cost)
