# Problema da mochila binária (ou knapsack problem)

Esse problema consiste em selecionar um subconjunto de itens, cada um com um peso e um valor, de modo que o valor total seja maximizado sem exceder a capacidade da mochila (um limite de peso).

Como o Algoritmo Genético em Bits pode ser aplicado: Cada indivíduo (genoma) é uma solução potencial, representada como uma sequência de bits. Cada bit indica se um determinado item está (1) ou não está (0) na mochila. A função de aptidão será ajustada para calcular o valor total dos itens selecionados, garantindo que o peso não exceda a capacidade da mochila. A população evolui, selecionando as combinações de itens mais valiosas, cruzando essas combinações e aplicando mutação para explorar novas combinações.

## Restrições

* Um objeto de cada tipo
* Objetos inteiros, ou seja, não pode ser fracionado
* Capacidade máxima deve ser respeitada
* Capacidade de carga associada a um número máximo de objetos

## Parâmetros do problema

```python
POPULATION_SIZE = 10
GENOME_SIZE = 8
MUTATION_SIZE = 0.1
GENERATIONS = 20
BACKPACK_SIZE = 15
```

## Definindo os itens

Cada item tem um peso e um valor (peso, valor)

```python
items_for_backpack = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10), (4, 7), (2, 6), (1, 2)]
```

# Disclaimer

Adaptação minha, mas código e documentação iniciais oferecidos pelo professor Claudinei Dias, da discplina de Inteligência Artifial no Centro Universitário Católica de Santa Catarina em Joinville. Ambos itens iniciais feitos em aula sobre o assunto.
