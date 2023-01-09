'''
Combinações de letras de um número de telefone
Dada uma string contendo dígitos de 2 a 9 inclusive, retorne todas as combinações de letras possíveis que o número 
pode representar. Devolva a resposta em qualquer ordem.

Um mapeamento de dígitos para letras (assim como nos botões do telefone) é dado abaixo. Observe que 1 não mapeia 
para nenhuma letra.

Examples
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

Notes
N/A
'''
import combination

def menu():

    print("=-" * 26)
    print("=-" * 3 + " Letter Combinations of a Phone Number! " + "=-" * 3)
    print("=-" * 26)

    numbers = str(input("Type the numbers: "))

    result = combination.combination(numbers)

    print(result)


if(__name__ == "__main__"):
    menu()