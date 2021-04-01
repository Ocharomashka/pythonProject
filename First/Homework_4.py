request = int(input("Введите целое положительное число: "))

num = request%10
request = request//10
while request > 0:
    if request%10 > num:
        num = request%10
    request= request//10
print("Самая большая цифра в числе: ", num)

