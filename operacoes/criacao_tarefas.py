import datetime
from auxiliares.auxiliares import validar_parametros, visualizar_unica_tarefa
from auxiliares import lista
def criar_tarefa(titulo: str, data_entrega: datetime, prioridade: str) -> None:
    #Cria uma nova tarefa com título e data de entrega, e prioridade opcional (padrão 2 - Média).
    lista_tarefas = lista.pegar_lista()
    
    if prioridade is None:
        prioridade = 'media'  # Prioridade padrão é Média
    try:
        validar_parametros(titulo, data_entrega, prioridade, None)
    except Exception as e:
        print(e)

    nova_tarefa = {
        "id": len(lista_tarefas) + 1, # percorre a lista_tarefas e puxa o ID mais recente, depois, soma +1 para a nova tarefa
        "descricao": titulo,
        "data_entrega": data_entrega,
        "prioridade": prioridade.capitalize(),
        "concluida": False
    }
    lista_tarefas.append(nova_tarefa)
    visualizar_unica_tarefa(nova_tarefa)
    return nova_tarefa