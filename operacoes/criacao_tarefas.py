import datetime
from auxiliares import auxiliares

# ENUM PRIORIDADE: 
# 1 - Baixa
# 2 - Média
# 3 - Alta

#lista temporaria. Só para teste.
lista_tarefas = [
    {
        "id": 1,
        "descricao": "Estudar Python",
        "data_entrega": "2024-06-30",
        "prioridade": 3,
        "concluida": False
    }
]

# função para validar dados de entrada
def validar_parametros(titulo: str, data_entrega, prioridade, id) -> None:
    #Valida as variaveis e lança ValueError se forem inválidos.
    
    if titulo is None or not isinstance(titulo, str) or titulo.strip() == "":
        raise ValueError("Título inválido: não pode ser nulo ou vazio.")
    if data_entrega is None:
        raise ValueError("Data de entrega inválida: não pode ser nula.")
    if not isinstance(data_entrega, datetime.date):
        raise ValueError("Data de entrega deve ser um datetime.date.")
    hoje = datetime.date.today()
    if data_entrega <= hoje:
        raise ValueError("Data de entrega deve ser posterior à data de hoje.")
    if prioridade not in [1, 2, 3]:
        raise ValueError("Prioridade inválida: deve ser 1 (Baixa), 2 (Média) ou 3 (Alta).")
    if id is not None and (not isinstance(id, int) or id <= 0):
        raise ValueError("ID inválido: deve ser um inteiro positivo.")

# função para criar uma nova tarefa
def criar_tarefa(titulo: str, data_entrega: datetime, prioridade: int) -> None:
    #Cria uma nova tarefa com título e data de entrega, e prioridade opcional (padrão 2 - Média).
    if prioridade is None:
        prioridade = 2  # Prioridade padrão é Média
    validar_parametros(titulo, data_entrega, prioridade, None)
    
    nova_tarefa = {
        "id": len(lista_tarefas) + 1,
        "descricao": titulo,
        "data_entrega": data_entrega,
        "prioridade": prioridade,
        "concluida": False
    }
    lista_tarefas.append(nova_tarefa)
    auxiliares.visualizar_unica_tarefa(nova_tarefa)
    return nova_tarefa

# Exemplo de uso
nova = criar_tarefa("Fazer exercícios", datetime.date(2025, 12, 5), 2)
print(nova)