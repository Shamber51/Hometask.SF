per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = list(per_cent.values())
money = int(input('Укажите сумму вклада под проценты'))
a1 = int(money * a[0])
a2 = int(money * a[1])
a3 = int(money * a[2])
a4 = int(money * a[3])
deposit = [a1,a2,a3,a4]
print(deposit)
deposit_max = max(deposit)
print(deposit_max)



