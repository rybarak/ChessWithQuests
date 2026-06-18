class Figurka:
    def __init__(self, nazev: str, barva: int):
        self.nazev = nazev
        self.barva = barva  # 1 = bílá, 0 = černá
        self.vektor = []
        self.vektory_utoku = []