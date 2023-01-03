'''
Espetos de churrasco

Você está no comando da churrasqueira. Uma espetada vegetariana é uma espetada que só tem legumes (-o). 
Um espeto não vegetariano é um espeto com pelo menos um pedaço de carne (-x).

["--xo--x--ox--",
"--xx--x--xx--",
"--oo--o--oo--",      <<< vegetarian skewer
"--xx--x--ox--",
"--xx--x--ox--"]

Por exemplo, a grelha abaixo tem 4 espetos não vegetarianos e 1 espeto vegetariano (o do meio).

Exemplos
Dada uma churrasqueira,
escreva uma função que retorne [# espetos vegetarianos, # espetos não vegetarianos]. No exemplo acima, a função 
deve retornar [1, 4].

[
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
] ➞ [2, 3]

[
  "--oooo-ooo--",
  "--xxxxxxxx--",
  "--o---",
  "-o-----o---x--",
  "--o---o-----"
) ➞ [3, 2]
'''

import barbecue
import time

def menu():
    print("=-" * 18)
    print("=-" * 5 + " Steakhouse " + "=-" * 5)
    print("=-" * 18)

    print("We are preparing the barbecue!")
    time.sleep(5)
    print(barbecue.barbecue_grill())

if(__name__ == "__main__"):
    menu()
    