from class_ship import ship

class cruise(ship):
    passengersWeight=2.25
    def __init__(self, draft, crew, passengers=0):#pongo 0 por defecto por si no me pasan nada
        super().__init__(self,draft,crew)
        self.passengers = passengers
      ##  try:
        ##    ship.check_type(draft)
       ##     ship.check_type(crew)
       ##     ship.check_type(passengers)
       ## except ValueError:
        ##    return


    def calculate_weight(self):
        weight=self.draft-self.crew*ship.crewWeight-self.passengers*cruise.passengersWeight
        return weight