from enum import IntEnum

class OpcoesMenuEnum(IntEnum):
    SAIR = 0
    LIMPAR_CONSOLE = 9
    VISUALIZAR_TAREFAS = 1
    CADASTRAR_TAREFA = 2
    ATUALIZAR_TAREFA = 3
    EXCLUIR_TAREFA = 4

class OpcoesMenuVisualizarEnum(IntEnum):
    SAIR = 0
    VISUALIZAR_TODAS = 1
    VISUALIZAR_POR_ID = 2
    VISUALIZAR_VENCIDAS = 3
    VISUALIZAR_PROXIMAS = 4

class OpcoesMenuExcluirEnum(IntEnum):
    SAIR = 0
    EXCLUIR_TODAS = 1
    EXCLUIR_POR_ID = 2

class OpcoesConfirmarExcluirEnum(IntEnum):
    SIM = 1
    NAO = 2

class OpcoesMenuAtualizarEnum(IntEnum):
    SAIR = 0
    DESCRICAO = 1
    DATA_ENTREGA = 2
    PRIORIDADE = 3
    STATUS_CONCLUSAO = 4