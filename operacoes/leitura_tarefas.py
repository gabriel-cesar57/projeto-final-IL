from datetime import datetime, timedelta
from exception import ContinuarComMenuException
from auxiliares import lista, auxiliares

def visualizar_todas_tarefas() -> list[dict[str, any]]:
    lista_tarefas = lista.pegar_lista()

    if len(lista_tarefas) > 0:
        auxiliares.visualizar_lista_tarefas(lista_tarefas)
        return lista_tarefas
    else:
        raise ContinuarComMenuException('Nenhuma tarefa cadastrada.')

def visualizar_tarefa_por_id(id: int) -> dict[str, any]:
    lista_tarefas = lista.pegar_lista()
    tarefa = next((t for t in lista_tarefas if t['id'] == id), None)

    if tarefa:
        auxiliares.visualizar_unica_tarefa(tarefa)
        return tarefa
    else:
        raise ContinuarComMenuException(f'Nenhuma tarefa com o ID {id} foi encontrada.')

def visualizar_tarefas_vencidas() -> list[dict[str, any]]:
    lista_tarefas = lista.pegar_lista()
    hoje = datetime.now().date()
    tarefas_vencidas = []

    for tarefa in lista_tarefas:
        data_entrega = auxiliares.formatar_data_para_datetime_date(tarefa['data_entrega'])

        if(not tarefa['concluida'] and data_entrega < hoje):
            tarefas_vencidas.append(tarefa)

    if(len(tarefas_vencidas) == 0):
        raise ContinuarComMenuException('Nenhuma tarefa vencida.')
    else:
        auxiliares.visualizar_lista_tarefas(tarefas_vencidas)
        return tarefas_vencidas

def visualizar_tarefas_prioridade(prioridade: str) -> list[dict[str, any]]:
    lista_tarefas = lista.pegar_lista()
    tarefas_prioridade = [t for t in lista_tarefas if t["prioridade"].lower() == prioridade.lower()]

    if(len(tarefas_prioridade) == 0):
        raise ContinuarComMenuException('Nenhuma tarefa encontrada com a prioridade indicada.')
    else:
        auxiliares.visualizar_lista_tarefas(tarefas_prioridade)
        return tarefas_prioridade

def visualizar_tarefas_proximas() -> list[dict[str, any]]:
    lista_tarefas = lista.pegar_lista()
    hoje = datetime.now().date()
    limite_superior = hoje + timedelta(days=3)
    tarefas_proximas = []

    for tarefa in lista_tarefas:
        data_entrega = auxiliares.formatar_data_para_datetime_date(tarefa['data_entrega'])
        if not tarefa['concluida'] and hoje <= data_entrega <= limite_superior:
            tarefas_proximas.append(tarefa)

    if not tarefas_proximas:
        raise ContinuarComMenuException('Nenhuma tarefa encontrada para os próximos 3 dias.')
    else:
        auxiliares.visualizar_lista_tarefas(tarefas_proximas)
        return tarefas_proximas