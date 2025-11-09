from typing import List, Dict, Any, Union
from datetime import datetime
from auxiliares import formatar_data_datetime, visualizar_unica_tarefa

def atualizar_tarefa(lista_tarefas: List[Dict[str, Any]], id_tarefa: int) -> None:
    """
    Localiza uma tarefa pelo ID e permite que o usuário atualize seus atributos.
    
    Args:
        lista_tarefas: A lista de dicionários contendo todas as tarefas.
        id_tarefa: O ID da tarefa que será atualizada.
    """
    
    # 1. Localizar a tarefa pelo ID
    tarefa_para_atualizar = next((t for t in lista_tarefas if t['id'] == id_tarefa), None)

    if not tarefa_para_atualizar:
        print(f'\nERRO: Nenhuma tarefa com o ID {id_tarefa} foi encontrada para atualização.')
        return

    print(f'\n--- TAREFA ATUAL (ID: {id_tarefa}) ---')
    visualizar_unica_tarefa(tarefa_para_atualizar)
    print('-' * 30)

    # 2. Loop para escolher e aplicar as atualizações
    while True:
        print("\nEscolha o campo para atualizar (ou 'Sair' para finalizar):")
        print("1 - Descrição")
        print("2 - Data de Entrega (dd/mm/aaaa)")
        print("3 - Prioridade (Baixa, Média, Alta)")
        print("4 - Status de Conclusão")
        print("S - Sair e Salvar Alterações")

        escolha = input("Opção: ").strip().upper()

        if escolha == 'S':
            break

        if escolha == '1':
            nova_descricao = input("Nova descrição: ").strip()
            if nova_descricao:
                tarefa_para_atualizar['descricao'] = nova_descricao
                print("Descrição atualizada.")
            else:
                print("Descrição não pode ser vazia. Nenhuma alteração feita.")

        elif escolha == '2':
            nova_data_str = input("Nova data de entrega (dd/mm/aaaa): ").strip()
            if nova_data_str:
                try:
                    # Tenta formatar para validar. Se funcionar, atribui a string.
                    formatar_data_datetime(nova_data_str)
                    tarefa_para_atualizar['data_entrega'] = nova_data_str
                    print("Data de entrega atualizada.")
                except ValueError:
                    print("ERRO: Formato de data inválido. Use dd/mm/aaaa.")
            else:
                print("Nenhuma alteração feita na data.")

        elif escolha == '3':
            prioridades_validas = ['BAIXA', 'MÉDIA', 'ALTA']
            nova_prioridade = input("Nova prioridade (Baixa, Média, Alta): ").strip().upper()
            if nova_prioridade in prioridades_validas:
                tarefa_para_atualizar['prioridade'] = nova_prioridade.capitalize()
                print(f"Prioridade alterada para {tarefa_para_atualizar['prioridade']}.")
            else:
                print("ERRO: Prioridade inválida. Use Baixa, Média ou Alta.")

        elif escolha == '4':
            status_atual = tarefa_para_atualizar['concluida']
            novo_status = input(f"Marcar como CONCLUÍDA? (Sim/Não). Status atual: {'Sim' if status_atual else 'Não'}: ").strip().upper()
            
            if novo_status in ('SIM', 'S'):
                tarefa_para_atualizar['concluida'] = True
                print("Status alterado para CONCLUÍDA.")
            elif novo_status in ('NÃO', 'N', 'NAO'):
                tarefa_para_atualizar['concluida'] = False
                print("Status alterado para NÃO CONCLUÍDA.")
            else:
                print("Escolha inválida. Nenhuma alteração feita no status.")

        else:
            print("Opção inválida. Por favor, escolha um número ou 'S'.")
            
    # 3. Exibir a tarefa após a atualização
    print(f'\n--- TAREFA ATUALIZADA (ID: {id_tarefa}) ---')
    visualizar_unica_tarefa(tarefa_para_atualizar)
    print("Atualização concluída com sucesso.")

if __name__ == '__main__':
    # Exemplo de uso (Para testar esta função isoladamente)
    
    # Mock da lista de tarefas
    lista_tarefas_exemplo = [
        {'id': 1, 'descricao': 'Terminar o código de Create', 'data_entrega': '20/10/2024', 'prioridade': 'Alta', 'concluida': False},
        {'id': 2, 'descricao': 'Revisar a documentação', 'data_entrega': '15/10/2024', 'prioridade': 'Média', 'concluida': False},
    ]

    # Tentativa de atualizar uma tarefa que existe
    print("--- Teste 1: Atualizar Tarefa 1 ---")
    atualizar_tarefa(lista_tarefas_exemplo, 1)

    # Tentativa de atualizar uma tarefa que não existe
    print("\n--- Teste 2: Atualizar Tarefa 99 ---")
    atualizar_tarefa(lista_tarefas_exemplo, 99)