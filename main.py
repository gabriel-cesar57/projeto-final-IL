# Linha 1: Título e equipe
# Linha 2: Introdução ao projeto (objetivo, escopo)
# Comentários abaixo serão removidos posteriormente

# ORGANIZAÇÃO: Cada membro pode criar uma parte do CRUD, tendo um membro com pelo menos dois tipos de ação. 
# Os commits serão feitos em branches específicas para a funcionalidade a ser criada.
# Os membros que ficaram com apenas um tipo de ação podem escolher também entre ajudar na especificação dos menus do sistema
# e verificar se todos os requisitos pedidos foram atingidos.

# DOCUMENTAÇÃO: A documentação pode ser feita em conjunto e com IA
# Podemos incluir o passo a passo para execução do sistema, além da explicação dos componentes

# ESTRUTURA: O sistema deve ser modular, separando bem cada etapa em funções
# É interessante que tudo no código seja tipado, para fins de legibilidade e organização
# Se for necessário, podemos criar arquivos separados para dividir os métodos utilizados
# Esse arquivo será o responsável por definir o fluxo do usuário, é importante que ele seja o mais enxuto possível

# BOAS PRÁTICAS: pastas e arquivos sempre com nomes minúsculos, seguindo a snake_case

# JOÃO: Read e Delete
# GABRIEL: Create e Refinamento
# MURILO: Update e Integração com menus
from auxiliares import enums
import exception
from menu import menu_principal

def executar() -> None:
    while True:
        try:
            print('\n=== SISTEMA DE GERENCIAMENTO DE TAREFAS ===\nSeja bem vindo. Como gostaria de prosseguir?')
            opcao_escolhida = int(input(menu_principal.pegar_opcoes_menu_principal()).strip())

            opcao_formatada = enums.OpcoesMenuEnum(opcao_escolhida)

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

executar()