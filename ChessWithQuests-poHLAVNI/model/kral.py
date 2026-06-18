from figurka import Figurka
class Kral(Figurka):
    def __init__(self, barva: int):
        super().__init__("Král", barva)
        self.skok = False
        self.vektor = [(1, 0),(-1, 0),(0, 1),(0, -1),(1, 1),(1, -1),(-1, 1),(-1, -1)]
        self.vektory_utoku = self.vektor.copy()