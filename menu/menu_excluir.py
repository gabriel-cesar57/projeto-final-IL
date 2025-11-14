from auxiliares import enums
import exception

def menu_excluir() -> None:
    while True:
        try:
            print('\n=== EXCLUIR TAREFAS ===')
            opcao_escolhida = int(input(pegar_opcoes_menu_excluir()).strip())

            opcao_formatada = enums.OpcoesMenuExcluirEnum(opcao_escolhida)

            processar_opcao_menu_excluir(opcao_formatada)
        except ValueError:
            print('Opção escolhida é inválida. Tente novamente.')
            continue
        except exception.ContinuarComMenuException as continuar:
            print(continuar)
            continue
        except exception.FecharMenuException as fechar:
            print(fechar)
            break

def pegar_opcoes_menu_excluir() -> str:
    return (
        '[1] Excluir todas as tarefas\n'
        '[2] Excluir tarefa por ID\n'
        '[0] Sair do menu de exclusão de tarefas\n'
        '\nDigite a opção escolhida: '
    )

def processar_opcao_menu_excluir(opcao: int) -> None:
    match opcao:
        case 0:
            raise exception.FecharMenuException('Usuário decidiu sair do menu de exclusão de tarefas. Voltando...')
        case 1:
            print('oi')
        