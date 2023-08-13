from class_ship import ship
class cargo (ship):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = cargo
        self.quality = quality
    def calculate_weight(self):
        cargo_aux=0
        if(self.quality==1):
            cargo_aux=3.5
        elif (self.quality==0.5):
            cargo_aux=2
        elif(self.quality==0.25):
            cargo_aux=0.5
        else:
            raise ValueError("Valor de calidad invalido")

        #self.cargo?
        weight=self.draft-self.crew*1.5-self.cargo*cargo_aux
        return weight