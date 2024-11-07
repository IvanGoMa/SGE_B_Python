
# 2. Dia de la setmana
# Crear un arxiu nou per a que retorni per pantalla la resposta adeqüada. Crear 1 variable per dia de la setmana.
# Exemple: dia_setmana = “dilluns”. Si dia_setmana és dilluns, haurà de sortir un print indicant “Avui és dilluns”.
# Si dia_setmana és dimarts, haurà de sortir per pantalla el text Avui és dimarts, etc. Per tant, caldrà utilitzar 
# l’expressió if de manera que si la variable dia_setmana es modifica indiqui el dia adeqüat.

dia_setmana = dimecres
if dia_setmana == "dillluns":
    print('Avui és dilluns')
elif dia_setmana == "dimarts":
    print('Avui és dimarts')
elif dia_setmana == "dimecres":
    print('Avui és dimecres')
elif dia_setmana == "dijous":
    print('Avui és dijous')
elif dia_setmana == "divendres":
    print('Avui és divendres')
elif dia_setmana == "dissabte":
    print('Avui és dissabte')
else:
    print('Avui és diumenge') 
