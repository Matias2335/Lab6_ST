
def calcular_imc(peso, altura):
    if peso <= 0:
        raise ValueError("O peso deve ser positivo.")

    if altura <= 0:
        raise ValueError("A altura deve ser positiva.")

    return peso / (altura ** 2)


def categorizar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    else:
        return "obesidade"


def classificar_pessoa(peso, altura):
    imc = calcular_imc(peso, altura)
    return categorizar_imc(imc)
