from datetime import datetime

# Visualizar todas as tarefas;
# Visualizar tarefa baseado em id;
# Visualizar as 3 tarefas mais próximas;
# Visualizar tarefas vencidas;
# Visualizar tarefas de um único tipo de prioridade.

def visualizar_todas_tarefas(lista_tarefas: list) -> None:
    for tarefa in lista_tarefas:
        print(f'{'='*5} TAREFA {tarefa["id"]} {'='*5}\n')
        print(f'Descrição: {tarefa['descricao']}')
        print(f'Data de entrega: {tarefa['data_entrega']}')
        print(f'Prioridade da tarefa: {tarefa['prioridade']}')
        print(f'Foi concluída?: {'Sim' if tarefa['concluida'] else 'Não'}')
        print(f'{'='*15}')

def visualizar_tarefa_por_id(lista_tarefas: list, id: int) -> None:
    print()

def visualizar_tarefas_vencidas(lista_tarefas: list) -> None:
    tarefas_vencidas = [t for t in lista_tarefas if t['concluida'] == False]

    if(len(tarefas_vencidas) == 0):
        print('Nenhuma tarefa vencida.')
    else:
        visualizar_todas_tarefas(tarefas_vencidas)

def visualizar_tarefas_prioridade(lista_tarefas: list, prioridade: str) -> None:
    tarefas_prioridade = [t for t in lista_tarefas if t["prioridade"].lower() == prioridade.lower()]

    if(len(tarefas_prioridade) == 0):
        print('Nenhuma tarefa encontrada com essa prioridade.')
    else:
        visualizar_todas_tarefas(tarefas_prioridade)

def visualizar_tarefas_proximas(lista_tarefas: list) -> None:
    print()