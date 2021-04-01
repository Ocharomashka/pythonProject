request = int(input("Введите число: "))

number = str(request)

number_two = number+number
number_three = number+number+number

answ_one = int(number)
answ_two = int(number_two)
answ_three = int (number_three)

print('{} + {} + {} = '.format(answ_one,answ_two,answ_three), answ_one+answ_two+answ_three)