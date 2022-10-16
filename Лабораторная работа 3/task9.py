salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 меся

i = salary - 6000
for need_money in range(months-1):
    spend *= 1.03
    b = salary - spend


need_money = - (i + b)

print(round(need_money))









