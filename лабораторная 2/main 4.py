salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
months -= 1
need_money += salary-spend
while months > 0:
    months -= 1
    spend = spend + spend * increase
    need_money += salary -spend
# TODO Оформить решение

print(round(abs(need_money)))
