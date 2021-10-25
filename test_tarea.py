import pytest
import numpy as np
import tarea

def test_hola():
    assert tarea.hola_mundo() == "Hola Mundo!"


@pytest.mark.parametrize("input, expected", [(1, 3), (10, 12), (-4, -2)])
def test_suma_dos(input, expected):
    assert tarea.suma_dos(input) == expected


def test_zero_array():
    return np.testing.assert_allclose(tarea.arreglo_de_ceros(100), np.zeros(shape=(100,)))
