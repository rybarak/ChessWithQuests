from figurka import Figurka
class Strelec(Figurka):
    def __init__(self, barva: int):
        super().__init__("Střelec", barva)
        self.skok = False
        self.vektor = [(1, 1),(1, -1),(-1, 1),(-1, -1)]
        self.vektory_utoku = self.vektor.copy()