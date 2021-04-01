income = int(input("Введите значение выручки фирмы на 2020 год, тыс. руб.: "))
costs = int(input("Введите значение издержек фирмы за 2020 год, тыс. руб.: "))
profit = income-costs
loss = costs-income
if income > costs:
    print("Значение прибыли в 2020 году составляет: ", profit, " тыс. руб.")
    print("Рентабельность в 2020 году составила: ", profit/income)
elif income < costs:
    print("Убыток в 2020 году составил: ", loss, " тыс. руб." )
else:
    print("Вы вышли в ноль!")

staff = int(input("Введите количество сотрудников: "))
profit_per = profit/staff
print("Прибыль фирмы в расчете на одного сотрудника составляет: ", profit_per, " тыс. руб." )