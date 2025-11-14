import exception
from operacoes import leitura_tarefas, atualizacao_tarefas
from auxiliares.enums import OpcoesMenuAtualizarEnum

def menu_atualizar(id_tarefa: int) -> None:
    tarefa_para_atualizar = leitura_tarefas.visualizar_tarefa_por_id(id_tarefa)
    while True:
        try:
            escolha_usuario = int(input(pegar_opcoes_menu_atualizar()).strip())
            escolha_formatada = OpcoesMenuAtualizarEnum(escolha_usuario)

            atualizacao_tarefas.atualizar_tarefa(tarefa_para_atualizar, escolha_formatada)
        except ValueError:
            print('Opção escolhida é inválida. Tente novamente.')
            continue
        except exception.ContinuarComMenuException as continuar:
            print(continuar)
            continue
        except exception.FecharMenuException as fechar:
            print(fechar)
            break

def pegar_opcoes_menu_atualizar() -> str:
    return (
        '\nATUALIZAÇÃO DE TAREFA\n'
        '[1] Descrição\n'
        '[2] Data de Entrega (dd/mm/aaaa)\n'
        '[3] Prioridade (Baixa, Média, Alta)\n'
        '[4] Status de Conclusão\n'
        '[0] Sair do menu de atualização e concluir alterações\n'
        '\nDigite a opção escolhida: '
    )