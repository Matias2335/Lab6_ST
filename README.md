# Exercício 4 — Tabela de Decisão para Frete Grátis

## Objetivo

Implementar uma função que determine se uma compra tem direito a frete grátis, utilizando três condições: valor da compra, assinatura premium e peso do pedido.

O frete grátis é concedido somente quando todas as três condições são satisfeitas simultaneamente.

## 1. Condições e resultado

| Identificador | Condição |
|---|---|
| C1 | Valor da compra ≥ R$ 200 |
| C2 | Cliente possui assinatura premium |
| C3 | Peso do pedido ≤ 30 kg |
| Resultado | Frete grátis quando C1, C2 e C3 são verdadeiras |

## 2. Tabela de decisão completa

Como existem três condições binárias, são possíveis oito combinações.

| Regra | C1: Compra ≥ R$ 200 | C2: Premium | C3: Peso ≤ 30 kg | Frete grátis |
|---|---|---|---|---|
| R1 | Sim | Sim | Sim | Sim |
| R2 | Não | Sim | Sim | Não |
| R3 | Sim | Não | Sim | Não |
| R4 | Sim | Sim | Não | Não |
| R5 | Não | Não | Sim | Não |
| R6 | Não | Sim | Não | Não |
| R7 | Sim | Não | Não | Não |
| R8 | Não | Não | Não | Não |

Apenas a regra R1 concede frete grátis. Nas demais regras, pelo menos uma condição obrigatória não é satisfeita.

## 3. Redução da tabela por *don't care*

A técnica *don't care* permite indicar condições que não precisam ser avaliadas em determinada regra, pois não alteram o resultado.

O símbolo "–" indica que a condição pode ser verdadeira ou falsa sem mudar o resultado daquela regra.

| Regra reduzida | C1: Compra ≥ R$ 200 | C2: Premium | C3: Peso ≤ 30 kg | Resultado |
|---|---|---|---|---|
| A | Sim | Sim | Sim | Frete grátis |
| B | Não | – | – | Frete cobrado |
| C | Sim | Não | – | Frete cobrado |
| D | Sim | Sim | Não | Frete cobrado |

## 4. Justificativa da redução

- **Regra A:** as três condições são verdadeiras; portanto, o frete é grátis.
- **Regra B:** quando a compra é inferior a R$ 200, o frete é cobrado, independentemente da assinatura premium e do peso.
- **Regra C:** quando a compra atinge R$ 200, mas o cliente não possui assinatura premium, o frete é cobrado, independentemente do peso.
- **Regra D:** quando a compra atinge R$ 200 e o cliente possui assinatura premium, mas o peso ultrapassa 30 kg, o frete é cobrado.

A tabela reduzida representa todas as oito combinações possíveis da tabela completa, agrupando as regras que apresentam o mesmo resultado.

## 5. Testes

A suíte de testes utiliza parametrização para cobrir as oito regras da tabela completa, com identificadores de R1 a R8.

Os testes verificam se a função `tem_frete_gratis(valor_compra, cliente_premium, peso)` retorna `True` somente quando as três condições são satisfeitas simultaneamente.

## Conclusão

A tabela de decisão completa permite verificar todas as combinações das condições. A redução por *don't care* simplifica a representação das regras sem alterar o resultado esperado do sistema.
