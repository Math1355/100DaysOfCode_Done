'''
Par de meias
Joseph está fazendo as malas para as férias. Ele está tendo um pouco de dificuldade para encontrar todas as suas meias, no entanto.

Escreva uma função que retorne o número de pares de meias que ele possui. Um par de meias consiste em duas letras iguais, como "AA". As meias são representadas como uma sequência não ordenada.

Examples
SockPairs("AA") ➞ 1

SockPairs("ABABC") ➞ 2

SockPairs("CABBACCC") ➞ 4

SockPairs("DABBACCC") ➞ 3

Notas
Se for dada uma string vazia (sem meias na gaveta), retorne 0.
Pode haver vários pares do mesmo tipo de meia, como dois pares de CC para o último exemplo.
'''

import socks_counter
from random import choice

def menu():

    print("=-" * 17)
    print("=-" * 4 + " Find the Socks! " + "=-" * 4)
    print("=-" * 17)

    #Places to look for socks
    place_1 = "AA"
    place_2 = "ABABC"
    place_3 = "CABBACCC"
    place_4 = "DABBACCC"
    place_5 = "DABBACCCEEEEE"
    place_6 = ""

    #List of all the places to look
    places = [place_1, place_2, place_3, place_4, place_5, place_6]

    #Choosing a place to search
    searching = choice(places)

    #Looking for how many pairs of socks are in this place
    result = socks_counter.Counter(searching)

    #Presenting the result
    print(result)

if(__name__ == "__main__"):
    menu()