from exception import ContinuarComMenuException
import datetime
import os

def limpar_console() -> None:
    """Limpa o terminal (Windows: cls, outros: clear)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar_data_para_datetime_date(data_nao_formatada: str)  -> datetime.date:
    return datetime.datetime.strptime(data_nao_formatada, '%d/%m/%Y').date()

def formatar_data_para_string(data_em_datetime_date: datetime.date) -> str:
    return data_em_datetime_date.strftime('%d/%m/%Y')

# função para validar dados de entrada
def validar_parametros(titulo: str, data_entrega: datetime, prioridade: str, id: int) -> None:
    #Valida as variaveis e lança ContinuarComMenuException se forem inválidos.
    
    if titulo is None or not isinstance(titulo, str) or titulo.strip() == "":
        raise ContinuarComMenuException("ERRO: Título não pode ser nulo ou vazio.")
    if data_entrega is None:
        raise ContinuarComMenuException("ERRO: Data de entrega não pode ser nula.")
    if not isinstance(data_entrega, datetime.date):
        raise ContinuarComMenuException("ERRO: Data de entrega deve ser no formato dd/mm/aaaa.")
    hoje = datetime.date.today()
    if data_entrega <= hoje:
        raise ContinuarComMenuException("ERRO: Data de entrega deve ser posterior à data de hoje.")
    if prioridade.lower().strip() not in ['baixa', 'media', 'média', 'alta']:
        raise ContinuarComMenuException("ERRO: Prioridade deve ser Baixa, Media ou Alta.")
    if id is not None and (not isinstance(id, int) or id <= 0):
        raise ContinuarComMenuException("ERRO: ID deve ser um inteiro positivo.")

def visualizar_lista_tarefas(lista_tarefas: list) -> None:
    for tarefa in lista_tarefas:
        print(f"{'='*5} TAREFA {tarefa['id']} {'='*5}\n")
        print(f'Descrição: {tarefa["descricao"]}')
        print(f'Data de entrega: {tarefa["data_entrega"]}')
        print(f'Prioridade da tarefa: {tarefa["prioridade"]}')
        print(f'Foi concluída?: {"Sim" if tarefa["concluida"] else "Não"}')
        print(f'{"="*20}')
    print(f'Final da listagem. Número de tarefas listadas: {len(lista_tarefas)}')


def visualizar_unica_tarefa(tarefa: dict) -> None:
    print(f"{'='*5} TAREFA {tarefa['id']} {'='*5}\n")
    print(f'Descrição: {tarefa["descricao"]}')
    print(f'Data de entrega: {tarefa["data_entrega"]}')
    print(f'Prioridade da tarefa: {tarefa["prioridade"]}')
    print(f'Foi concluída?: {"Sim" if tarefa["concluida"] else "Não"}')
    print(f'{"="*15}')