from operacoes import criacao_tarefas

def menu_cadastrar() -> dict[str, any]:
    titulo = input('Digite o título da tarefa: ')
    data_entrega = input('Digite a data de entrega [FORMATO OBRIGATÓRIO: dd/MM/yyyy]: ')
    prioridade = input('Digite a prioridade da tarefa [Baixa / Media / Alta]: ')

    criacao_tarefas.criar_tarefa(titulo, data_entrega, prioridade)