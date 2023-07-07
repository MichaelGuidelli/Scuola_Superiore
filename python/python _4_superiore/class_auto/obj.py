class Auto:
    
    numero_di_auto = 0
    
    def __init__(self, modello: str, colore: str):
        self.modello = modello
        self.colore = colore
        
        Auto.numero_di_auto += 1
        
    def carta_di_circolazione(self):
        
        return f"Modello: {self.modello}, Colore: {self.colore}"