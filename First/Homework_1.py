number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
action = input("""
               + для сложения
               - для вычитания
               / для деления
               * для умножения : """)
if action == "+":
    print('{} + {} = '.format(number_one, number_two))
    print(number_one+number_two)

elif action == "-":
    print('{} - {} = '.format(number_one, number_two))
    print(number_one - number_two)

elif action == "/":
    print('{} / {} = '.format(number_one, number_two))
    print(number_one / number_two)

else:
    print('{} * {} = '.format(number_one, number_two))
    print(number_one * number_two)