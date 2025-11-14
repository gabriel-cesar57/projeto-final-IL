from auxiliares import lista, enums, auxiliares
from exception import ContinuarComMenuException
from operacoes import leitura_tarefas

def excluir_todas_tarefas() -> list[dict[str, any]]:
    lista_tarefas = lista.pegar_lista()

    if len(lista_tarefas) > 0:
        confirmar_formatado = entrada_usuario_confirmar_acao()

        if confirmar_formatado == enums.OpcoesConfirmarExcluirEnum.SIM:
            lista_tarefas.clear()
            print('Lista de tarefas foi esvaziada com sucesso.')
            return lista_tarefas
        else:
            print('Esvaziamento da lista foi cancelado. Voltando...')
            return lista_tarefas
    else:
        raise ContinuarComMenuException('Lista já está vazia.')
    
def excluir_tarefa_por_id(id: int) -> list[dict[str, any]]:
    lista_tarefas = lista.pegar_lista()

    if len(lista_tarefas) > 0:
        tarefa = leitura_tarefas.visualizar_tarefa_por_id(id)
        confirmar_formatado = entrada_usuario_confirmar_acao()

        if confirmar_formatado == enums.OpcoesConfirmarExcluirEnum.SIM:
            lista_tarefas.remove(tarefa)
            print('Tarefa excluída com sucesso.')
            return lista_tarefas
        else:
            print('Exclusão da tarefa foi cancelado. Voltando...')
            return lista_tarefas
    else:
        raise ContinuarComMenuException('Lista não contém nenhuma tarefa.')
            
def entrada_usuario_confirmar_acao() -> enums.OpcoesConfirmarExcluirEnum:
    confirmar_limpar = int(input(pegar_texto_confirmar_excluir()).strip())
    return enums.OpcoesConfirmarExcluirEnum(confirmar_limpar)

def pegar_texto_confirmar_excluir() -> str:
    return (
        'Tem certeza que deseja fazer isso? Essa ação é IRREVERSÍVEL.\n'
        '[1] SIM\n'
        '[2] NÃO\n'
        '\nDigite a opção escolhida: '
    )