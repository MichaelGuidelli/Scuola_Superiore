class Auto:
    
    macchine_in_gara = 0
    tipologia_motore = "Aspirato"
    
    def __init__(self, modello: str, colore: str, prezzo: int):
        self.modello = modello
        self.colore = colore
        self.prezzo = prezzo
        
        Auto.macchine_in_gara += 1
        
    def carta_di_circolazione(self):
        
        return f"Modello: {self.modello.capitalize()}, Colore: {self.colore.capitalize()}, Prezzo: {self.prezzo}€, tipologia motore: {Auto.tipologia_motore}"