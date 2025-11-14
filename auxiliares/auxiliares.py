import datetime

def formatar_data_datetime(data_nao_formatada: str)  -> datetime:
    return datetime.datetime.strptime(data_nao_formatada, '%d/%m/%Y')

# função para validar dados de entrada
def validar_parametros(titulo: str, data_entrega: datetime, prioridade: str, id: int) -> None:
    #Valida as variaveis e lança ValueError se forem inválidos.
    
    if titulo is None or not isinstance(titulo, str) or titulo.strip() == "":
        raise ValueError("ERRO: Título não pode ser nulo ou vazio.")
    if data_entrega is None:
        raise ValueError("ERRO: Data de entrega não pode ser nula.")
    if not isinstance(data_entrega, datetime.date):
        raise ValueError("Data de entrega deve ser no formato ANO/MES/DIA.")
    hoje = datetime.date.today()
    if data_entrega <= hoje:
        raise ValueError("ERRO: Data de entrega deve ser posterior à data de hoje.")
    if prioridade.lower() not in ['baixa', 'media', 'alta']:
        raise ValueError("ERRO: Prioridade deve ser Baixa, Media ou Alta.")
    if id is not None and (not isinstance(id, int) or id <= 0):
        raise ValueError("ERRO: ID deve ser um inteiro positivo.")

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