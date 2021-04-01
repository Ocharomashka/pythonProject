second = int(input("Сколько секунд у вас есть?  "))

hh=second//3600
mm=(second//60)%60
ss=(second%60)

if ss < 10:
    ss=str("0"+str(ss))
else:
    ss=str(ss)
if mm< 10:
    mm=str("0" + str(mm))
else:
    mm=str(mm)
print(str(hh) + ":" + str(mm) + ":" + str(ss))