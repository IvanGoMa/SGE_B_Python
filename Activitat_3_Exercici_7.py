variable = 82
comprovant = 100

while comprovant <= 400:
    if comprovant == variable:
        print("La variable está entre 100 i 400")
        break
    comprovant += 1
if comprovant > 400:
    print("La variable no està entre 100 i 400")
