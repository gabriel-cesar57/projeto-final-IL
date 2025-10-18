from datetime import datetime

def formatar_data_datetime(data_nao_formatada: str)  -> datetime:
    return datetime.strptime(data_nao_formatada, '%d/%m/%Y')

def visualizar_lista_tarefas(lista_tarefas: list) -> None:
    for tarefa in lista_tarefas:
        print(f'{'='*5} TAREFA {tarefa["id"]} {'='*5}\n')
        print(f'Descrição: {tarefa['descricao']}')
        print(f'Data de entrega: {tarefa['data_entrega']}')
        print(f'Prioridade da tarefa: {tarefa['prioridade']}')
        print(f'Foi concluída?: {'Sim' if tarefa['concluida'] else 'Não'}')
        print(f'{'='*20}')
    print(f'Final da listagem. Número de tarefas listadas: {len(lista_tarefas)}')

def visualizar_unica_tarefa(tarefa: dict) -> None:
    print(f'{'='*5} TAREFA {tarefa["id"]} {'='*5}\n')
    print(f'Descrição: {tarefa['descricao']}')
    print(f'Data de entrega: {tarefa['data_entrega']}')
    print(f'Prioridade da tarefa: {tarefa['prioridade']}')
    print(f'Foi concluída?: {'Sim' if tarefa['concluida'] else 'Não'}')
    print(f'{'='*15}')