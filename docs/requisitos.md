# Requisitos do Sistema — Projeto Final IL  
Sistema de Gestão de Tarefas Acadêmicas

Este documento descreve os requisitos funcionais e não funcionais do sistema.

---

## 1. Objetivo do Sistema

Permitir que o usuário gerencie tarefas acadêmicas de forma simples, utilizando um sistema em Python baseado em menu.  
As operações incluem criar, visualizar, editar e excluir tarefas, além de registrar progresso e prioridade.

---

## 2. Escopo

O sistema opera em ambiente local, em memória durante a execução (sem persistência automática entre execuções).  
Não exige instalação de bibliotecas externas e funciona via terminal.

---

## 3. Requisitos Funcionais (RF)

### **RF01 — Criar tarefas**  
O sistema deve permitir cadastrar uma nova tarefa contendo:
- título    
- prioridade  
- prazo (data)  
- progresso (concluído/pendente)

### **RF02 — Listar tarefas**  
O sistema deve exibir todas as tarefas existentes com:
- ID  
- título / descrição  
- prioridade  
- progresso  
- prazo

### **RF03 — Editar tarefa**  
O usuário deve poder modificar qualquer atributo da tarefa:
- título / descrição  
- prioridade  
- prazo  
- progresso

### **RF04 — Excluir tarefa**  
O sistema deve permitir:
- remover uma tarefa pelo ID.  
- remover todas as tarefas (com confirmação).

### **RF05 — Validar entradas**  
O sistema deve validar:
- prioridade (Baixa / Media / Alta)  
- progresso : concluido (sim) / pendente (não)  
- campos obrigatórios não vazios  
- formatos de data suportados (dd/mm/aaaa ou dd-mm-aaaa)

### **RF06 — Persistência**  
O sistema NÃO realiza persistência automática entre execuções — todos os dados existem somente em memória durante a execução.  
Exportação/importação manual pode ser adicionada futuramente, mas não faz parte do escopo atual.

### **RF07 — Exibir menu interativo**  
O sistema deve apresentar um menu ao usuário com opções numéricas claras.

---

## 4. Requisitos Não Funcionais (RNF)

### **RNF01 — Usabilidade**
- Interface baseada em texto, simples e intuitiva.  
- Todas as mensagens devem ser claras e objetivas.

### **RNF02 — Portabilidade**
- Deve funcionar em qualquer sistema com Python 3.10+.

### **RNF03 — Confiabilidade**
- Em caso de erro, o programa deve exibir mensagem adequada sem corromper estado em memória.

### **RNF04 — Manutenibilidade**
- Código dividido em módulos (menu, operações, auxiliares, exceptions).  
- Estrutura clara para facilitar modificações futuras.

### **RNF05 — Desempenho**
- Operações rápidas, adequadas para uso local e volume pequeno de tarefas.

### **RNF06 — Segurança**
- Não requer autenticação.  
- Deve evitar quebra do programa por entradas inválidas.  
- Exceções personalizadas devem ser usadas para controle de fluxo do menu.

---

## 5. Regras de Negócio (RN)

### **RN01 — IDs únicos**
Cada tarefa deve possuir um identificador numérico único, atribuído automaticamente ao criar.

### **RN02 — Progresso**
O progresso é booleano/conclusão: `concluida = True` (concluída) ou `False` (pendente).  
Não é permitido criar uma tarefa já marcada como concluída; novas tarefas iniciam com `concluida = False`.

### **RN03 — Prioridade**
Prioridade aceita: **Baixa**, **Media**, **Alta**.  
Valores são normalizados pelo sistema (capitalização) e `Media` é padrão quando não informado.

### **RN04 — Prazo**
Prazo deve ser informado no formato `DD/MM/AAAA` e ser posterior à data atual — tanto na criação quanto na atualização.

### **RN05 — Exclusões**
Exclusão de todas as tarefas exige confirmação explícita do usuário.

---

## 6. Dependências

Nenhuma biblioteca externa é necessária.  
O projeto utiliza apenas módulos padrões do Python.

---

## 7. Restrições

- O sistema não possui interface gráfica.  
- Não possui múltiplos usuários ou autenticação.  
- Armazenamento é limitado à memória durante a execução (sem salvamento automático).

---
