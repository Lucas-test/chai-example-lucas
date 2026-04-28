import sys
sys.path.append("src")

import pytest
from losange import Losange

def test_calcul_aire_losange():
    losange = Losange(6, 4)
    assert losange.get_area() == 12

def test_diagonales_negatives():
    with pytest.raises(ValueError):
        Losange(-6, 4)