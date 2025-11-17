# Introdução a Lógica: Sistema de gestão de tarefas acadêmicas

Este projeto visa implementar um sistema simples e completo de gerenciamento de tarefas por parte de um ou mais alunos. Os alunos devem ter a capacidade de visualizar, criar, atualizar e deletar tarefas, além de definir configurações como prazos, prioridades e progresso. As tarefas podem ser incluídas em relatórios ou classificações específicas. 

Desenvolvido como projeto final da disciplina **IL — Lógica de Programação**.


# Funcionalidades

- Criar tarefas com título, descrição, prioridade e prazo  
- Listar tarefas cadastradas  
- Editar atributos de uma tarefa  
- Marcar progresso (concluído/pendente)  
- Excluir tarefas  
- Interface simples baseada em menu (CLI)



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


# Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/gabriel-cesar57/projeto-final-IL
```

2. Entre na pasta:

```bash
cd projeto-final-IL
```

3. Execute o programa:

```bash
python main.py
```


# Tecnologias utilizadas

Python 3.10+


# Licença

Projeto acadêmico — livre para estudo e modificação.