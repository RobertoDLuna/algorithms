"""
Requisito 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca) - Passos a se seguir:

1 - Descobrir o maior horário com pessoas acessando a plataforma
2 - Para isso usarei as seguintes informações:
2.1 - A função irá receber uma lista de tuplas onde cada tupla
    registra o horário de entrada e saída de cada estudante = lista_tupla = permanence_period
2.2 - A função também irá receber uma variável que vai ser chamada
    várias vezes com valores diferentes
3 - Algoritmo deve usar solução iterativa
4 - Caso o target_time passado seja nulo, o valor retornado deve ser None
    Ex: 0 é um valor nulo
5 - Se permanece_period receber uma entrada inválida retornar None
6 - Retornar a quantidade de estudantes presentes para uma entrada específica

Lógica a se seguir:
1 - Verificar se target_time é nulo
2 - Percorrer a lista e verificar se os valores de entrada e saída são nulos
3 - Criar uma variável que vai somar + 1 sempre que determinado valor condizer
    com o tempo de entrada - saída
"""


def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    users_online = 0

    # para cada intervalo de entrada e saida em permanence_period
    for init_time, end_time in permanence_period:
        #se não tiver entrada ou saida, retorna none
        if not init_time or not end_time:
            return None
        if init_time <= target_time <= end_time:
            users_online += 1
    return users_online

# Testando Manualmente
permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_periods, 1))