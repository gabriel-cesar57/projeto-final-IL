from auxiliares.enums import OpcoesMenuEnum
from menu import menu_visualizar, menu_excluir, menu_atualizar, menu_cadastrar
from auxiliares import auxiliares
import exception

def menu_principal() -> None:
    auxiliares.limpar_console()
    while True:
        try:
            print('\n=== SISTEMA DE GERENCIAMENTO DE TAREFAS ===\nSeja bem vindo. Como gostaria de prosseguir?\n')
            opcao_escolhida = int(input(menu_principal.pegar_opcoes_menu_principal()).strip())

            opcao_formatada = OpcoesMenuEnum(opcao_escolhida)

            menu_principal.processar_opcao_menu_principal(opcao_formatada)
        except ValueError:
            print('Opção escolhida é inválida. Tente novamente.')
            continue
        except exception.ContinuarComMenuException as continuar:
            print(continuar)
            continue
        except exception.FecharMenuException as fechar:
            print(fechar)
            break
        except KeyboardInterrupt:
            print('Interrompendo programa...')
            break
        except Exception as e:
            print(e)
            print('Um erro inesperado ocorreu. Tente novamente.')
            continue

def pegar_opcoes_menu_principal() -> str:
    return (
        '[1] Visualizar tarefa(s)\n'
        '[2] Cadastrar tarefa\n'
        '[3] Atualizar tarefa\n'
        '[4] Excluir tarefa(s)\n'
        '[9] Limpar console\n'
        '[0] Sair do programa\n'
        '\nDigite a opção escolhida: '
    )

def processar_opcao_menu_principal(opcao: int) -> None:
    match opcao:
        case OpcoesMenuEnum.SAIR:
            raise exception.FecharMenuException('Usuário decidiu encerrar o programa. Fechando...')
        case OpcoesMenuEnum.LIMPAR_CONSOLE:
            auxiliares.limpar_console()
        case OpcoesMenuEnum.VISUALIZAR_TAREFAS:
            menu_visualizar.menu_visualizar()
        case OpcoesMenuEnum.CADASTRAR_TAREFA:
            menu_cadastrar.menu_cadastrar()
        case OpcoesMenuEnum.ATUALIZAR_TAREFA:
            menu_atualizar.menu_atualizar()
        case OpcoesMenuEnum.EXCLUIR_TAREFA:
            menu_excluir.menu_excluir()