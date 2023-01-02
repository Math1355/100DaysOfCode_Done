'''
Procurando Nemo
Você recebe uma sequência de palavras. Você precisa encontrar a palavra "Nemo", e retornar uma string 
como esta: I found Nemo at [a ordem da palavra que você encontra nemo]!.

Se você não encontrar o Nemo, volte Não consigo encontrar o Nemo :(.

Exemplos
findNemo("Estou encontrando o Nemo !") ➞ "Encontrei o Nemo às 4!"

findNemo("Nemo sou eu") ➞ "Encontrei Nemo em 1!"
findNemo("Eu sou o Nemo") ➞ "Encontrei o Nemo às 2!"

Notas
! , ? . são sempre separados da última palavra.
O Nemo sempre se parecerá com o Nemo, e não com o NeMo ou outras variações de capital.
Nemo's, ou qualquer coisa que diga Nemo com algo atrás, não conta como Procurando Nemo.
Se houver vários Nemo na frase, retorne apenas para o primeiro.'''

import find_nemo

def menu():
    print("=-" * 18)
    print("=-" * 5 + " FIND NEMO " + "=-" * 5)
    print("=-" * 18)

    text = str(input("Write where to look for Nemo: "))
    result = find_nemo.nemo(text)

    print(result)

if(__name__ == "__main__"):
    menu()