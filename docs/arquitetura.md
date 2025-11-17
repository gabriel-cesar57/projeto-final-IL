# Documentação da API Interna  
Sistema de Gestão de Tarefas Acadêmicas

Este documento descreve as funções, classes e módulos utilizados no projeto.  
A API é totalmente interna e voltada ao uso dentro do próprio sistema.

---

# 1. Estrutura de Módulos
# Estrutura do Projeto
projeto-final-IL/
│ main.py
│ README.md
│
├─docs/
| requisitos.md
| arquitetura.md
|
├─ menu/
│ menu_atualizar.py
│ menu_cadastrar.py
| menu_excluir.py
| menu_principal.py
| menu_vizualizar.py
| 
├─ operacoes/
│ criacao_tarefas.py
| atualizacao_tarefas.py
| excluir_tarefas.py
| leitura_tarefas.py
│
├─ auxiliares/
│ auxiliares.py
│ enums.py
| lista.py
│
└─ exception/
| exception.py

# Módulo main.py

Descrição:
Ponto de entrada do sistema; inicializa o menu principal.

Fluxo básico:

    Carrega tarefas do arquivo

    Exibe o menu

    Mantém loop até o usuário sair

3. # Módulo menu

Descrição:
Exibe as opções disponíveis e direciona o usuário para a operação correspondente.

Opções suportadas:

[1] Visualizar tarefa(s)
[2] Cadastrar tarefa
[3] Atualizar tarefa
[4] Excluir tarefa(s)
[9] Limpar console
[0] Sair do programa

4. # Módulo operacoes

**criacao_tarefas.py**
Descrição:
Coleta dados do usuário e cria uma nova tarefa.

Entrada (input via terminal):

título
descrição
prioridade
prazo

**atualizacao_tarefas.py**

Descrição:
Edita qualquer atributo de uma tarefa existente, solicitando o id da tarefa alvo.

Parâmetros:

id (int) → ID da tarefa a ser modificada.

Retorno:
Nenhum.
(Alterações são persistidas automaticamente.)

**excluir_tarefas.py**

Descrição:
Exclui qualquer tarefa existente, solicitando o id da tarefa alvo.
Ou realiza a exclusão de todas as tarefas.

Parâmetros:

id → ID da tarefa a ser excluida.



**leitura_tarefas.py**

Descrição:
Retorna todas as tarefas armazenadas.

Retorno:

lista_tarefas contendo dicionários de tarefas.



5. # Módulo Auxiliares

**auxiliares.py**

<h3> função limpar_console() </h3>
Descrição:
Limpa o terminal do sistema operacional.

Windows → cls

Linux/Mac → clear

<h3> função formatar_data_datetime(data_nao_formatada) </h3>
Descrição:
Converte uma data no formato DD/MM/AAAA para um objeto datetime.

Parâmetros:

data_nao_formatada (str) — string no formato "25/12/2025".

Retorno:

datetime.datetime correspondente à data informada.

Erros possíveis:

ValueError se o formato for inválido.

<h3> função validar_parametros(titulo, data_entrega, prioridade, id) </h3>

Descrição:
Valida os dados de entrada antes de criar ou editar uma tarefa.
Se qualquer dado for inválido, lança ValueError.

Parâmetros:
titulo (str): não pode ser vazio
data_entrega (datetime.date): deve ser posterior ao dia atual
prioridade (str): deve ser "Baixa", "Media" ou "Alta"
id (int): deve ser inteiro positivo, se informado

Erros possíveis:
ValueError se qualquer validação falhar.

<h3> função visualizar_lista_tarefas(lista_tarefas) </h3>

Descrição:
Exibe no terminal todas as tarefas contidas na lista recebida.

Parâmetros:
lista_tarefas (list): lista de dicionários contendo as tarefas.

Formato exibido:

ID
descrição
data de entrega
prioridade
concluída (Sim/Não)

<h3> função visualizar_unica_tarefa(tarefa)</h3>
Descrição:
Exibe no terminal os detalhes de apenas uma tarefa.

Parâmetros:
tarefa (dict) contendo:
id
descricao
data_entrega
prioridade
concluida

6. # Módulo Enums
Nele estão armazenados classes que representam todas as opções de menu do sistema,  
garantindo organização, padronização e evitando valores "mágicos" no código.

7. # Módulo lista
Lista global que armazena todas as tarefas cadastradas.
Cada tarefa deve ser um dicionário contendo campos como:
```python
{
    "id": int,
    "descricao": str,
    "data_entrega": datetime | str,
    "prioridade": str, #Baixa, Media ou Alta
    "concluida": bool
}
```

8. # Módulo Exception

**classe ContinuarComMenuException**

Descrição:
Exceção usada para informar ao loop principal do menu que ele deve continuar a execução sem encerrar e sem quebrar o fluxo.
Utilizada quando o usuário executa alguma ação que não encerra o menu.
E quando é necessário "pular" para o próximo ciclo do loop sem efeitos colaterais.

**classe FecharMenuException**
Descrição:
Exceção usada para indicar que o menu deve ser encerrado imediatamente, finalizando o loop principal.
