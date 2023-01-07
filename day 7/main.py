'''
Mesclar Matriz Ordenada
Dadas duas matrizes inteiras classificadas nums1 e nums2, mescle nums2 em nums1 como uma matriz classificada.

Exemplos
Entrada:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Saída: [1,2,2,3,5,6]
Restrições
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
Notas
O número de elementos inicializados em nums1 e nums2 são m e n respectivamente.
Você pode assumir que nums1 tem espaço suficiente (tamanho igual a m + n) para conter elementos adicionais de nums2.
'''

import merge

def menu():

    print("=-" * 17)
    print("=-" * 3 + " Merge Sorted Array! " + "=-" * 3)
    print("=-" * 17)

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]

    result = merge.merge(nums1, nums2)

    print(result)


if(__name__ == "__main__"):
    menu()