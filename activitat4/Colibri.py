class Colibri:
    def __init__(self,tamany,especie,color,habitat,pes):
        self.tamany = tamany
        self.especie = especie
        self.color = color
        self.habitat = habitat
        self.pes = pes

    def getTamany(self):
        return self.tamany
    def setTamany(self,newTamany):
        self.tamany= newTamany

    def getEspecie(self):
        return self.especie
    def setEspecie(self,newEspecie):
        self.especie= newEspecie

    def getColor(self):
        return self.color
    def setColor(self,newColor):
        self.color= newColor

    def getHabitat(self):
        return self.habitat
    def setHabitat(self,newHabitat):
        self.habitat= newHabitat

    def getPes(self):
        return self.pes
    def setPes(self,newPes):
        self.pes= newPes