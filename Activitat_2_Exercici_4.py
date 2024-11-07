
# 4. Aplicar IVA segons el salari
# En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
# Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. Si el salari és menor de 30.000 
# s’aplica un 10% de l’iva. Si el salari és menor a 60.000 s’aplica un IVA del 21%.

#Exemple càlcul si el salari son 5000 => 5.000 * 0/100

salari = 20000
if salari < 15000:
    print(f"S'aplica un IVA del 0%, el salari final és {salari}")
elif salari < 30000:
    salariFinal = salari - salari*0.1
    print(f"S'aplicarà un IVA del 10%, el salari final és {salariFinal} ")
else:
    salariFinal = salari - salari*0.21
    print(f"S'aplica un IVA del 21%, el salari final és {salariFinal}")
