class Losange {
  constructor(diagonale1, diagonale2) {
    if (diagonale1 <= 0 || diagonale2 <= 0) {
      throw new Error("Les diagonales doivent être positives");
    }

    this.diagonale1 = diagonale1;
    this.diagonale2 = diagonale2;
  }

  getArea() {
    return (this.diagonale1 * this.diagonale2) / 2;
  }
}

module.exports = Losange;