from auxiliares import enums
from menu import menu_visualizar, menu_excluir, menu_atualizar, menu_cadastrar
import exception

def pegar_opcoes_menu_principal() -> str:
    return (
        '[1] Visualizar tarefa(s)\n'
        '[2] Cadastrar tarefa\n'
        '[3] Atualizar tarefa\n'
        '[4] Excluir tarefa(s)\n'
        '[0] Sair do programa\n'
        '\nDigite a opção escolhida: '
    )

def processar_opcao_menu_principal(opcao: int) -> None:
    match opcao:
        case enums.OpcoesMenuEnum.SAIR:
            raise exception.FecharMenuException('Usuário decidiu encerrar o programa. Fechando...')
        case enums.OpcoesMenuEnum.VISUALIZAR_TAREFAS:
            menu_visualizar.menu_visualizar()
        case enums.OpcoesMenuEnum.CADASTRAR_TAREFA:
            menu_cadastrar.menu_cadastrar()
        case enums.OpcoesMenuEnum.ATUALIZAR_TAREFA:
            menu_atualizar.menu_atualizar()
        case enums.OpcoesMenuEnum.EXCLUIR_TAREFA:
            menu_excluir.menu_excluir()