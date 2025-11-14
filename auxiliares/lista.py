lista_tarefas: list[dict[str, any]] = [
    {'id': 1, 'descricao': 'oi', 'data_entrega': '12/01/2012',
     'prioridade': 'alta', 'concluida': True},
     {'id': 2, 'descricao': 'oi', 'data_entrega': '12/01/2012',
     'prioridade': 'alta', 'concluida': False},
     {'id': 3, 'descricao': 'oi', 'data_entrega': '15/11/2025',
     'prioridade': 'alta', 'concluida': False}]

def pegar_lista() -> list[dict[str, any]]:
    return lista_tarefas