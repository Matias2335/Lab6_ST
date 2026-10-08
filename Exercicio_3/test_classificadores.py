
import pytest
from classificadores import classificar_vento


@pytest.mark.parametrize(
    "velocidade, resultado_esperado",
    [
        (10, "calmo"),
        (25, "moderado"),
        (50, "forte"),
        (70, "tempestade"),
    ],
    ids=[
        "classe-calmo",
        "classe-moderado",
        "classe-forte",
        "classe-tempestade",
    ],
)
def test_classes_vento(velocidade, resultado_esperado):
    assert classificar_vento(velocidade) == resultado_esperado


@pytest.mark.parametrize(
    "velocidade, resultado_esperado",
    [
        (19.99, "calmo"),
        (20, "moderado"),
        (39.99, "moderado"),
        (40, "forte"),
        (59.99, "forte"),
        (60, "tempestade"),
    ],
    ids=[
        "antes-de-20",
        "limite-20",
        "antes-de-40",
        "limite-40",
        "antes-de-60",
        "limite-60",
    ],
)
def test_valores_limite_vento(velocidade, resultado_esperado):
    assert classificar_vento(velocidade) == resultado_esperado
