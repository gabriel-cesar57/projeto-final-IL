# Introdução a Lógica: Sistema de gestão de tarefas acadêmicas

Este projeto visa implementar um sistema simples e completo de gerenciamento de tarefas por parte de um ou mais alunos. Os alunos devem ter a capacidade de visualizar, criar, atualizar e deletar tarefas, além de definir configurações como prazos, prioridades e progresso. As tarefas podem ser incluídas em relatórios ou classificações específicas. 

Desenvolvido como projeto final da disciplina **IL — Lógica de Programação**.

# Nomes:

Gabriel Cesar Gomes Pereira - 1143218602 <br>
Jõao Paulo Cota Santana - 1143289139 <br>
Murilo Ribeiro Santos - 1143339744 <br>

# Funcionalidades

- Criar tarefas com título, descrição, prioridade e prazo  
- Listar tarefas cadastradas  
- Editar atributos de uma tarefa  
- Marcar progresso (concluído/pendente)  
- Excluir tarefas  
- Interface simples baseada em menu (CLI)



# Estrutura do Projeto
projeto-final-IL/ <br>
│ main.py <br>
│ README.md <br>
│ <br>
├─docs/ <br>
| requisitos.md <br>
| arquitetura.md <br>
| <br>
├─ menu/ <br>
│ menu_atualizar.py <br>
│ menu_cadastrar.py <br>
| menu_excluir.py <br>
| menu_principal.py <br>
| menu_vizualizar.py <br>
|  <br>
├─ operacoes/ <br>
│ criacao_tarefas.py <br>
| atualizacao_tarefas.py <br>
| excluir_tarefas.py <br>
| leitura_tarefas.py <br>
│ <br>
├─ auxiliares/ <br>
│ auxiliares.py <br>
│ enums.py <br>
| lista.py <br>
│ <br>
└─ exception/ <br>
| exception.py <br>


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
