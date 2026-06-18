from figurka import Figurka
class Pesak(Figurka):
    def __init__(self, barva: int):
        super().__init__("Pěšák", barva)
        self.skok = False
        if barva == 1:  # bílý
            self.vektor = [(0, 1)]
            self.vektory_utoku = [(-1, 1),(1, 1)]
        else:  # černý
            self.vektor = [(0, -1)]
            self.vektory_utoku = [(-1, -1),(1, -1)]