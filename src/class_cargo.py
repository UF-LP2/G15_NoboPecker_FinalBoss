from class_ship import ship
class cargo (ship):
    # statics de los valores correspondientes a cada calidad de cargo
    value_quality1 = 3.5
    value_quality05 = 2
    value_quality025 = 0.5
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = cargo
        self.quality = quality
    def calculate_weight(self):
        cargo_aux=0
        if(self.quality==1):
            cargo_aux= self.value_quality1
        elif (self.quality==0.5):
            cargo_aux= self.value_quality05
        elif(self.quality==0.25):
            cargo_aux= self.value_quality025
        else:
            raise ValueError("Valor de calidad invalido")

        #self.cargo?
        weight=self.draft-self.crew*1.5-self.cargo*cargo_aux
        return weight