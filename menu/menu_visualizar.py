from auxiliares import enums
import exception
import operacoes.leitura_tarefas

def menu_visualizar() -> None:
    while True:
        try:
            print('\n=== VISUALIZAR TAREFA ===')
            opcao_escolhida = int(input(pegar_opcoes_menu_visualizar()).strip())

            opcao_formatada = enums.OpcoesMenuVisualizarEnum(opcao_escolhida)

            processar_opcao_menu_visualizar(opcao_formatada)
        except ValueError:
            print('Opção escolhida é inválida. Tente novamente.')
            continue
        except exception.ContinuarComMenuException as continuar:
            print(continuar)
            continue
        except exception.FecharMenuException as fechar:
            print(fechar)
            break

def pegar_opcoes_menu_visualizar() -> str:
    return (
        '[1] Visualizar todas as tarefas\n'
        '[2] Visualizar tarefa por ID\n'
        '[3] Visualizar tarefas vencidas\n'
        '[4] Visualizar tarefas próximas da data de entrega\n'
        '[0] Sair do menu de visualização de tarefas\n'
        '\nDigite a opção escolhida: '
    )

def processar_opcao_menu_visualizar(opcao: int) -> None:
    match opcao:
        case 0:
            raise exception.FecharMenuException('Usuário decidiu sair do menu de visualização de tarefas. Voltando...')
        case 1:
            # leitura_tarefas.
            print('oi')
        