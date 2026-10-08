
import pytest
from imc import categorizar_imc, calcular_imc


@pytest.mark.parametrize(
    "imc, resultado_esperado",
    [
        (18.49, "abaixo do peso"),
        (18.5, "peso normal"),
        (24.99, "peso normal"),
        (25.0, "sobrepeso"),
        (29.99, "sobrepeso"),
        (30.0, "obesidade"),
    ],
    ids=[
        "abaixo-de-18-5",
        "fronteira-18-5",
        "abaixo-de-25",
        "fronteira-25",
        "abaixo-de-30",
        "fronteira-30",
    ],
)
def test_valores_limite(imc, resultado_esperado):
    assert categorizar_imc(imc) == resultado_esperado


def test_peso_zero():
    with pytest.raises(ValueError):
        calcular_imc(0, 1.75)


def test_altura_zero():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)
