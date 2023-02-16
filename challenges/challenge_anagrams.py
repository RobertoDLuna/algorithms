"""
Requisito 4: Passos a se seguir
1 - Criar um algoritmo que compare duas strings e identifique se uma
    é anagrama da outra
2 - Deve ser case insensitve
Lógica a se pensar:
1 - Verificar se as strings são vazias, caso contrário retornar False
2 - Criar uma função que vai converter cada string para lista e realizar
    o sorting, trazendo essa lista ordenada como retorno da função
3 - Utilizarei o bubble sort para fazer a ordenação
"""


def string_sort(string):
    for i in range(len(string) - 1):
        for j in range(i+1, len(string)):
            if string[i] > string[j]:
                string[i], string[j] = string[j], string[i]
    return ''.join(string)


def equality_verify(word_1, word_2):
    if (word_1 == '' or word_2 == ''):
        return False
    return word_1 == word_2


def is_anagram(first_string, second_string):
    first_string_ordered = string_sort(list(first_string.lower()))
    second_string_ordered = string_sort(list(second_string.lower()))

    return (
        first_string_ordered,
        second_string_ordered,
        equality_verify(first_string_ordered, second_string_ordered)
    )
