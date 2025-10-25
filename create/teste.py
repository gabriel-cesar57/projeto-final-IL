import datetime



lista_tarefas = [
    {
        "id": 1,
        "descricao": "Estudar Python",
        "data_entrega": "2024-06-30",
        "prioridade": "alta",
        "concluida": False
    }
]

# função para criar uma nova tarefa

def criar_tarefa(titulo: str, data_entrega: datetime.date | str) -> dict:
    """Cria uma nova tarefa com título e data de entrega."""
    if isinstance(data_entrega, datetime.date):
        data_entrega_str = data_entrega.isoformat()
        """ Converte datetime.date para string no formato ISO (YYYY-MM-DD) """
    else:
        data_entrega_str = data_entrega
        """ Assume que já é uma string no formato correto """
    nova_tarefa = {
        "id": len(lista_tarefas) + 1,
        "descricao": titulo,
        "data_entrega": data_entrega_str,
        "prioridade": "média",
        "concluida": False
    }
    lista_tarefas.append(nova_tarefa)
    return nova_tarefa

# Exemplo de uso
nova = criar_tarefa("Fazer exercícios", datetime.date(2024, 7, 5))
print(nova)




