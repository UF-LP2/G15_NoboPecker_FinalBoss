class ship:
    def _init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        aux=self.calculate_weight
        if(aux>20):
            #saquear
        else:
            #exc

    def calculate_weight(self):
        weight=self.draft-self.crew*1.5
        return weight