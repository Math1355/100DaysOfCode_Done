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
import sys

def TrappingRainWater(altura):
    #armazena o tamanho da lista de armazenamento de agua
    n = len(altura)

    #Verifica se a lista não e menos igual a 2 se for não e possivel armazenar agua
    if n <= 2:
        return 0
    
    #total armazenado
    agua = 0

    #Monta uma lista nova com o 1 tamanho menor que a inserida
    left = [None] * (n - 1)
    #armazena o maximo do valor na primeira instancia da lista
    left[0] = -sys.maxsize

    #instancia o lado direito da lista com o mesmo valor do lado esquerdo acima
    right = -sys.maxsize

 
    #regra de limite para percorrer a lista
    if 0 <= n and n <= 3 * 104:
        #Vai percorrer a lista da esquerda para direita - 1 
        for i in range(1, n - 1):
            left[i] = max(left[i - 1], altura[i - 1])


        #pegar o maior valor da direita para esquerda   e verifica a quantidade de agua      
        for i in reversed(range(1, n - 1)):
            right = max(right, altura[i + 1])

            if min(left[i], right) > altura[i]:
                agua += min(left[i], right) - altura[i]


        
    
    return agua