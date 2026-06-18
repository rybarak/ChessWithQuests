from figurka import Figurka
class Kun(Figurka):
    def __init__(self, barva: int):
        super().__init__("Kůň", barva)
        self.skok = True
        self.vektor = [(1, 2),(2, 1),(-1, 2),(-2, 1),(1, -2),(2, -1),(-1, -2),(-2, -1)]
        self.vektory_utoku = self.vektor.copy()