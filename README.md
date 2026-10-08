# Exercício 3 — Classificação Genérica por Faixas

## Objetivo

Implementar uma função genérica capaz de classificar um valor de acordo com uma lista de faixas ordenadas. A função é utilizada para classificar tanto o IMC quanto a velocidade do vento.

## 1. Classes de equivalência do vento

A classificação do vento utiliza as seguintes faixas:

| Classe | Intervalo de velocidade | Resultado |
|---|---|---|
| Classe 1 | Velocidade < 20 | Calmo |
| Classe 2 | 20 ≤ velocidade < 40 | Moderado |
| Classe 3 | 40 ≤ velocidade < 60 | Forte |
| Classe 4 | Velocidade ≥ 60 | Tempestade |

Cada classe representa um conjunto de valores que recebe a mesma classificação.

## 2. Análise dos valores-limite

As fronteiras entre as classes são 20, 40 e 60. Para testar o comportamento nas fronteiras, são utilizados valores imediatamente inferiores e valores exatamente iguais aos limites.

| Fronteira | Valor testado | Resultado esperado |
|---|---:|---|
| 20 | 19,99 | Calmo |
| 20 | 20 | Moderado |
| 40 | 39,99 | Moderado |
| 40 | 40 | Forte |
| 60 | 59,99 | Forte |
| 60 | 60 | Tempestade |

Esses testes verificam se os valores são classificados corretamente antes e exatamente em cada fronteira.

## 3. Implementação genérica

A função `classificar_por_faixas(valor, faixas)` recebe um valor e uma lista de tuplas contendo o limite superior e o rótulo de cada faixa.

A função percorre as faixas ordenadas e retorna o rótulo correspondente ao primeiro limite superior maior que o valor informado.

A classificação do IMC e a classificação do vento utilizam essa mesma função genérica, alterando apenas suas respectivas tabelas de faixas.

## 4. Testes realizados

A suíte de testes contempla:

- Um representante de cada uma das quatro classes de equivalência do vento.
- Os seis casos de valores-limite das fronteiras 20, 40 e 60.
- A verificação dos resultados esperados para cada caso.

Os testes são parametrizados com identificadores descritivos para facilitar a identificação de falhas.

## Conclusão

A implementação permite reutilizar a mesma lógica de classificação em diferentes contextos, enquanto os testes verificam as classes de equivalência e os comportamentos nas fronteiras entre as faixas.
