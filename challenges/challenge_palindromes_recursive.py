"""
Requisito 3 - Passos a se seguir:
1 - A função recebe um parâmetro que é uma string
2 - Verificar se essa string é palíndromo ou não
    (lida da esquerda para direita e vice-versa)
3 - Se for passado uma string vazia, return False
4 - Se a palavra não for palíndromo, return False
5 - Se a palavra for palíndromo return True


Lógica a se pensar:
1 - Primeiro validar se a string vem vazia
2 - A função recebe 3 parâmetros: palavra, índice mínimo e índice máximo
3 - É palíndromo quando a primeira letra é igual a última, a segunda
    igual a penúltima e assim sucessivamente
4 - Logo sempre verificar se word[low_index] == word[high_index]
    Caso seja diferente, retornar False
5 - Chamar a própria função passando o menor índex + 1, maior índex - 1
6 - Quando o menor índice for maior que o maior índice, significa que a
    palavra já foi percorrida e os valores validados
"""


def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or word == "":
        return False

    if (word[low_index] != word[high_index]):
        return False

    if (low_index < high_index):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return True
