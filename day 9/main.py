'''
Capturando Água da Chuva
Dado n inteiros não negativos representando um mapa de elevação onde a largura de cada barra é 1, calcule quanta 
água ela pode reter depois de chover.

Exemplos
Exemplo 1:

Entrada: altura = [0,1,0,2,1,0,1,3,2,1,2,1]
Saída: 6
Explicação: O mapa de elevação acima (seção preta) é representado pela matriz [0,1,0,2,1,0,1,3,2,1,2,1].
Neste caso, 6 unidades de água da chuva (seção azul) estão sendo retidas.

Exemplo 2:

Entrada: altura = [4,2,0,3,2,5]
Saída: 9
Restrições
n == altura.comprimento
0 <= n <= 3 * 104
0 <= altura[i] <= 105
'''
from trapping_rain_water import TrappingRainWater

altura = [4, 2, 0, 3, 2, 5]
altura_2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
altura_3 = [5, 1, 2, 1, 3, 3, 5]

resultado = TrappingRainWater(altura_2)
print(resultado)
