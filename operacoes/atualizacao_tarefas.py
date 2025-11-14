from datetime import datetime
from auxiliares.auxiliares import formatar_data_datetime, visualizar_unica_tarefa
from auxiliares.enums import OpcoesMenuAtualizarEnum
from exception import FecharMenuException, ContinuarComMenuException

def atualizar_descricao(tarefa: dict[str, any]) -> None:
    """Solicita e atualiza a descrição da tarefa."""
    nova_descricao = input("Nova descrição: ").strip()
    if nova_descricao:
        tarefa['descricao'] = nova_descricao
        print("Descrição atualizada com sucesso. Voltando...")
    else:
        raise ContinuarComMenuException("ERRO: Descrição não pode ser vazia. Nenhuma alteração feita.")

def atualizar_data_entrega(tarefa: dict[str, any]) -> None:
    """Solicita e atualiza a data de entrega (valida com formatar_data_datetime)."""
    nova_data_str = input("Nova data de entrega (dd/mm/aaaa): ").strip()
    if nova_data_str:
        try:
            # valida a data; se válido, guarda como string no mesmo formato
            data_formatada = formatar_data_datetime(nova_data_str)
            if data_formatada < datetime.now():
                raise ContinuarComMenuException('ERRO: A data de entrega deve ser posterior à atual.')
            tarefa['data_entrega'] = data_formatada.date().strftime('%d/%m/%Y')
            print("Data de entrega atualizada.")
        except ValueError:
            raise ContinuarComMenuException("ERRO: Formato de data inválido. Use dd/mm/aaaa.")
    else:
        raise ContinuarComMenuException("ERRO: Data não pode ser vazia. Nenhuma alteração feita na data.")

def atualizar_prioridade(tarefa: dict[str, any]) -> None:
    """Solicita e atualiza a prioridade da tarefa (Baixa, Media, Alta)."""
    prioridades_validas = ['BAIXA', 'MEDIA', 'ALTA']
    nova_prioridade = input("Nova prioridade (Baixa, Media, Alta): ").strip().upper()
    if nova_prioridade in prioridades_validas:
        tarefa['prioridade'] = nova_prioridade.capitalize()
        print(f"Prioridade alterada para {tarefa['prioridade']}.")
    else:
        raise ContinuarComMenuException("ERRO: Prioridade inválida. Use Baixa, Media ou Alta.")

def atualizar_status_conclusao(tarefa: dict[str, any]) -> None:
    """Solicita e atualiza o status de conclusão da tarefa."""
    status_atual = tarefa.get('concluida', False)
    novo_status = int(input(f"Marcar como CONCLUÍDA?\n[1] Sim\n[2] Não\nStatus atual - {'[SIM]' if status_atual else '[NÃO]'}: ").strip())
    if novo_status == 1:
        tarefa['concluida'] = True
        print("Status alterado para CONCLUÍDA.")
    elif novo_status == 2:
        tarefa['concluida'] = False
        print("Status alterado para NÃO CONCLUÍDA.")
    else:
        raise ContinuarComMenuException("ERRO: Escolha inválida. Nenhuma alteração feita no status.")

def atualizar_tarefa(tarefa: dict[str, any], opcao_usuario: OpcoesMenuAtualizarEnum) -> dict[str, any]:
    """
    Executa a ação de atualização correspondente à opção do usuário.
    Levanta FecharMenuException quando a opção for SAIR.
    Retorna a tarefa atualizada.
    """
    match opcao_usuario:
        case OpcoesMenuAtualizarEnum.SAIR:
            raise FecharMenuException('Usuário decidiu sair do menu de atualização de tarefas. Voltando...')
        case OpcoesMenuAtualizarEnum.DESCRICAO:
            atualizar_descricao(tarefa)
        case OpcoesMenuAtualizarEnum.DATA_ENTREGA:
            atualizar_data_entrega(tarefa)
        case OpcoesMenuAtualizarEnum.PRIORIDADE:
            atualizar_prioridade(tarefa)
        case OpcoesMenuAtualizarEnum.STATUS_CONCLUSAO:
            atualizar_status_conclusao(tarefa)

    # Mostrar tarefa atualizada e retornar
    visualizar_unica_tarefa(tarefa)
    return tarefa