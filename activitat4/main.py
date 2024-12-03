from Colibri import Colibri
from Cotxe import Cotxe

# Creem 3 instàncies de cotxe
cotxe1 = Cotxe("Opel","Corsa","vermell",2005,5)
cotxe2 = Cotxe("Audi","A4","gris",2020, 5)
cotxe3 = Cotxe("Ferrari", "SF90","vermell",2022,4)

# Creem 3 instàncies de colibrí
colibri1 = Colibri(8,"Rutilante","verd","bosc",5)
colibri2 = Colibri(10,"Pard","marró","bosc",7)
colibri3 = Colibri(11,"Orejimorado", "verd","sabana",6)

# Mostrem 3 getters de cotxe
print(f"El cotxe 1 és un {Cotxe.getMarca(cotxe1)} {Cotxe.getModel(cotxe1)}")
print(f"El cotxe 2 és de color {Cotxe.getColor(cotxe2)}")
print(f"El cotxe 3 és de l'any {Cotxe.getAny(cotxe3)}")

# Mostrem 4 getters de colibrí
print(f"El colibrí 1 pesa {Colibri.getPes(colibri1)}g")
print(f"El colibri 2 medeix {Colibri.getTamany(colibri2)}cm")
print(f"El colibri 2 és de color {Colibri.getColor(colibri2)}")
print(f"El colibrí 3 viu a la {Colibri.getHabitat(colibri3)}")

# Modifiquem 2 atributs de cotxe
Cotxe.setColor(cotxe2,"groc")
Cotxe.setModel(cotxe1, "Astra")

# Mostrem els atributs canviats
print(f"Ara el cotxe 1 és un {Cotxe.getMarca(cotxe1)} {Cotxe.getModel(cotxe1)}")
print(f"Ara el cotxe 2 és de color {Cotxe.getColor(cotxe2)}")

# Modifiquem 2 atributs de colibrí
Colibri.setHabitat(colibri3,"selva")
Colibri.setPes(colibri1,8)

# Mostrem els atributs canviats
print(f"Ara el colibrí 1 pesa {Colibri.getPes(colibri1)}g")
print(f"Ara el colibrí 3 viu a la {Colibri.getHabitat(colibri3)}")