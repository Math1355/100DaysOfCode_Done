'''Próximo Prime
Dado um número inteiro, crie uma função que retorne o próximo primo. Se o número for primo, retorna o próprio 
número.

Examples
NextPrime(12) ➞ 13

NextPrime(24) ➞ 29

NextPrime(11) ➞ 11
// 11 é primo, então retornamos o próprio número.
Notas
N / D'''

import next_prime

def menu():

    print("=-" * 17)
    print("=-" * 4 + " Find the prime number! " + "=-" * 4)
    print("=-" * 17)

    number = int(input("Enter a number: "))

    next_number = next_prime.next_prime(number)

    print("O numero primo mais proximo e: {}".format(next_number))

if(__name__ == "__main__"):
    menu()