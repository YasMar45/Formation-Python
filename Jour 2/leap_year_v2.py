year = 2100

if year % 400 ==0:     #commencer avec ça obligatoirement
    print ("leap year")
elif not year % 100 == 0:
    print("no leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("no leap year")