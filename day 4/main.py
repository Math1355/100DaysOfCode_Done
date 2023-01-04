'''
Johnny está fazendo progresso?
Para treinar para uma próxima maratona, Johnny faz uma corrida de longa distância todos os sábados. Ele deseja rastrear com que frequência o número de milhas percorridas neste sábado excede o número de milhas percorridas no sábado anterior. Isso é chamado de dia de progresso.
Crie uma função que considere uma matriz de milhas percorridas todos os sábados e retorne o número total de dias de progresso de Johnny.

Exemplos
ProgressDays([3, 4, 1, 2]) ➞ 2
// Há dois dias de progresso, (3->4) e (1->2)

progressDays([10, 11, 12, 9, 10]) ➞ 3

progressDays([6, 5, 4, 3, 2, 9]) ➞ 1

progressDays([9, 9])  ➞ 0

Notas
Correr o mesmo número de milhas da semana passada não conta como um dia de progresso.
'''

import counter
from random import choice

def menu():
    print("=-" * 17)
    print("=-" * 4 + " Making Progress " + "=-" * 4)
    print("=-" * 17)

    week_1 = [10, 11, 12, 9, 10] #3 dias
    week_2 = [6, 5, 4, 3, 2, 9] #1 dia
    week_3 = [9, 9] #0 dias
    week_4 = [9, 9, 9, 10, 11] #2 dias

    weeks = [week_1, week_2, week_3, week_4]

    days = choice(weeks)

    result = counter.Progress_days(days)

    print("Johnny had {} days of progress!".format(result))

if(__name__ == "__main__"):
    menu()