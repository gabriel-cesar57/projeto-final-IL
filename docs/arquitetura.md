# Documentação da estrutura do projeto  
## Sistema de Gestão de Tarefas Acadêmicas

Este documento descreve os módulos utilizados no projeto.

---

# Estrutura do Projeto
- main.py
- README.md
- docs/
  - requisitos.md
  - arquitetura.md
- menu/
  - menu_principal.py
  - menu_visualizar.py
  - menu_cadastrar.py
  - menu_atualizar.py
  - menu_excluir.py
- operacoes/
  - criacao_tarefas.py
  - leitura_tarefas.py
  - atualizacao_tarefas.py
  - excluir_tarefas.py
- auxiliares/
  - auxiliares.py
  - enums.py
  - lista.py
- exception/
  - exception.py

Descrição breve por arquivo / módulo
- main.py — ponto de entrada; chama o menu principal ([menu/menu_principal.py](../menu/menu_principal.py)).
- menu/ — menus interativos; cada arquivo exibe opções e chama funções em operacoes:
  - [menu/menu_principal.py](../menu/menu_principal.py) — menu principal e roteamento.
  - [menu/menu_visualizar.py](../menu/menu_visualizar.py) — opções de visualização.
  - [menu/menu_cadastrar.py](../menu/menu_cadastrar.py) — coleta inputs e cria tarefa.
  - [menu/menu_atualizar.py](../menu/menu_atualizar.py) — fluxo para atualizar campos de uma tarefa.
  - [menu/menu_excluir.py](../menu/menu_excluir.py) — opções de exclusão (por ID / todas).
- operacoes/ — lógica de negócio (não cuida de input/print além do estritamente necessário):
  - [operacoes/criacao_tarefas.py](../operacoes/criacao_tarefas.py) — valida e cria tarefa (usa auxiliares.lista).
  - [operacoes/leitura_tarefas.py](../operacoes/leitura_tarefas.py) — funções de leitura/filtragem.
  - [operacoes/atualizacao_tarefas.py](../operacoes/atualizacao_tarefas.py) — atualiza campos da tarefa.
  - [operacoes/excluir_tarefas.py](../operacoes/excluir_tarefas.py) — remove tarefa(s).
- auxiliares/ — utilitários e armazenamento em memória:
  - [auxiliares/auxiliares.py](../auxiliares/auxiliares.py) — formatação, validações e helpers (ex.: limpar_console, formatar datas).
  - [auxiliares/enums.py](../auxiliares/enums.py) — IntEnum para opções de menu.
  - [auxiliares/lista.py](../auxiliares/lista.py) — lista única em memória e getter `pegar_lista()`.
- exception/ — exceções de controle de fluxo:
  - [exception/exception.py](../exception/exception.py) — `ContinuarComMenuException`, `FecharMenuException`.
