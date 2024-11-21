#    C1 : l'année est divisiblea par 4 sans être divisible par 100 (cas des années qui ne sont pas des multiples de 100)
#    C2 : l'année est divisible par 400 (cas des années multiples de 100).



#C1 = l'année est divisable par 4 ET/and NON/not par 100 (pas multiple de 100) OU/or #C2 : l'année est divisible par 400 (cas des années multiples de 100) = leap year
#Sinon no leap year

year = 2100
if (year % 4 == 0) and (not year % 100 == 0) or (year % 400 == 0):      #aussi (year % 100 != 0) pour dire que si le résultat est différent que 0, FALSE
    print("a leap year")

else:
    print("no a leap year")


