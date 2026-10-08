
def classificar_por_faixas(valor, faixas):
    for limite_superior, rotulo in faixas:
        if valor < limite_superior:
            return rotulo

    return faixas[-1][1]


FAIXAS_IMC = [
    (18.5, "abaixo do peso"),
    (25, "peso normal"),
    (30, "sobrepeso"),
    (float("inf"), "obesidade"),
]

FAIXAS_VENTO = [
    (20, "calmo"),
    (40, "moderado"),
    (60, "forte"),
    (float("inf"), "tempestade"),
]


def categorizar_imc(imc):
    return classificar_por_faixas(imc, FAIXAS_IMC)


def classificar_vento(velocidade):
    return classificar_por_faixas(velocidade, FAIXAS_VENTO)
