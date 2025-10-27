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

def criar_tarefa(titulo: str, data_entrega: datetime) -> None:
    """Cria uma nova tarefa com título e data de entrega."""
    # verificar se os parametros != nulo ou vazio
    # verificar se data > hoje
    # prioridade das tarefas com numeros
    
    nova_tarefa = {
        "id": len(lista_tarefas) + 1,
        "descricao": titulo,
        "data_entrega": data_entrega,
        "prioridade": "média",
        "concluida": False
    }
    lista_tarefas.append(nova_tarefa)
    auxiliares.visualizar_unica_tarefa(nova_tarefa)

# Exemplo de uso
nova = criar_tarefa("Fazer exercícios", datetime.date(2024, 7, 5))
print(nova)