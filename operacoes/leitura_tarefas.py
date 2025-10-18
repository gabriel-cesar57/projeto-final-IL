from datetime import datetime, timedelta
from auxiliares import auxiliares

def visualizar_tarefa_por_id(lista_tarefas: list, id: int) -> None:
    tarefa = next((t for t in lista_tarefas if t['id'] == id), None)

    if tarefa:
        auxiliares.visualizar_unica_tarefa(tarefa)
    else:
        print(f'Nenhuma tarefa com o ID {id} foi encontrada.')

def visualizar_tarefas_vencidas(lista_tarefas: list) -> None:
    hoje = datetime.now()
    tarefas_vencidas = []

    for tarefa in lista_tarefas:
        data_entrega = auxiliares.formatar_data_datetime(tarefa['data_entrega'])

        if(not tarefa['concluida'] and data_entrega < hoje):
            tarefas_vencidas.append(tarefa)

    if(len(tarefas_vencidas) == 0):
        print('Nenhuma tarefa vencida.')
    else:
        auxiliares.visualizar_lista_tarefas(tarefas_vencidas)

def visualizar_tarefas_prioridade(lista_tarefas: list, prioridade: str) -> None:
    tarefas_prioridade = [t for t in lista_tarefas if t["prioridade"].lower() == prioridade.lower()]

    if(len(tarefas_prioridade) == 0):
        print('Nenhuma tarefa encontrada com a prioridade indicada.')
    else:
        auxiliares.visualizar_lista_tarefas(tarefas_prioridade)

def visualizar_tarefas_proximas(lista_tarefas: list) -> None:
    hoje = datetime.now()
    limite_superior = hoje + timedelta(days=3)
    tarefas_proximas = []

    for tarefa in lista_tarefas:
        data_entrega = auxiliares.formatar_data_datetime(tarefa['data_entrega'])
        if not tarefa['concluida'] and hoje <= data_entrega <= limite_superior:
            tarefas_proximas.append(tarefa)

    if not tarefas_proximas:
        print('Nenhuma tarefa encontrada para os próximos 3 dias.')
    else:
        auxiliares.visualizar_lista_tarefas(tarefas_proximas)