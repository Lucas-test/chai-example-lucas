class Losange:
    def __init__(self, diagonale1, diagonale2):
        if diagonale1 <= 0 or diagonale2 <= 0:
            raise ValueError("Les diagonales doivent être positives")

        self.diagonale1 = diagonale1
        self.diagonale2 = diagonale2

    def get_area(self):
        return (self.diagonale1 * self.diagonale2) / 2