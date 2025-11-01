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

# função para criar uma nova tarefa
def criar_tarefa(titulo: str, data_entrega: datetime, prioridade: int) -> None:
    #Cria uma nova tarefa com título e data de entrega, e prioridade opcional (padrão 2 - Média).
    if prioridade is None:
        prioridade = 2  # Prioridade padrão é Média
    auxiliares.validar_parametros(titulo, data_entrega, prioridade, None)
    
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