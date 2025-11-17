# Requisitos do Sistema — Projeto Final IL  
Sistema de Gestão de Tarefas Acadêmicas

Este documento descreve os requisitos funcionais e não funcionais do sistema.

---

## 1. Objetivo do Sistema

Permitir que o usuário gerencie tarefas acadêmicas de forma simples, utilizando um sistema em Python baseado em menu.  
As operações incluem criar, visualizar, editar e excluir tarefas, além de registrar progresso e prioridade.

---

## 2. Escopo

O sistema opera em ambiente local, utilizando armazenamento em arquivo texto ou JSON.  
Não exige instalação de bibliotecas externas e funciona via terminal.

---

## 3. Requisitos Funcionais (RF)

### **RF01 — Criar tarefas**
O sistema deve permitir cadastrar uma nova tarefa contendo:
- título    
- prioridade  
- prazo
- progresso (concluído/pendente)

---

### **RF02 — Listar tarefas**
O sistema deve exibir todas as tarefas existentes com:
- ID  
- título  
- prioridade  
- progresso
- prazo

---

### **RF03 — Editar tarefa**
O usuário deve poder modificar qualquer atributo da tarefa:
- título  
- descrição  
- prioridade  
- prazo  
- progresso

---

### **RF04 — Excluir tarefa**
O sistema deve permitir remover uma tarefa pelo ID.
Ou remover todas as tarefas.
---

### **RF05 — Validar entradas**
O sistema deve validar:
- prioridade (Baixa / Media / Alta)  
- progresso : concluido (sim) / pendente (não)  
- campos obrigatórios não vazios  
- formatos de data suportados  

---

### **RF06 — Salvar e carregar dados automaticamente**
O sistema deve:
- salvar as alterações  
- carregar as tarefas ao executar o comando adequado.  

---

### **RF07 — Exibir menu interativo**
O sistema deve apresentar um menu ao usuário com opções numéricas claras.

---

## 4. Requisitos Não Funcionais (RNF)

### **RNF01 — Usabilidade**
- Interface baseada em texto, simples e intuitiva.  
- Todas as mensagens devem ser claras e objetivas.

---

### **RNF02 — Portabilidade**
- Deve funcionar em qualquer sistema com Python 3.10+.

---

### **RNF03 — Confiabilidade**
- Em caso de erro no arquivo, o programa deve exibir mensagem adequada.  
- Não deve corromper dados existentes.

---

### **RNF04 — Manutenibilidade**
- Código dividido em módulos (menu, operações, auxiliares, exceptions).  
- Estrutura clara para facilitar modificações futuras.

---

### **RNF05 — Desempenho**
- O sistema deve executar todas as operações rapidamente, sem atrasos perceptíveis.  
- Operações limitadas ao uso em arquivos locais, sem processamento pesado.

---

### **RNF06 — Segurança**
- Não requer autenticação.  
- Deve evitar quebra do programa por entradas inválidas.  
- Exceções personalizadas devem ser usadas para garantir integridade.

---

## 5. Regras de Negócio (RN)

### **RN01 — IDs devem ser únicos**
Cada tarefa deve possuir um identificador numérico único.

---

### **RN02 — Progresso**
O progresso deve ser um valor entre **concluida e pendente**, representando o status atual.

---

### **RN03 — Prioridade**
A prioridade é formatada automaticamente, indo de **Baixa, Media, Alta**, onde:
- Baixa = baixa prioridade  
- Media = média prioridade **(padrão caso nulo)** 
- Alta = alta prioridade  

---

### **RN04 — Prazo**
O prazo deve ser informado em formato de data definido no sistema (ex: `DD/MM/AAAA`).

---

## 6. Dependências

Nenhuma biblioteca externa é necessária.  
O projeto utiliza apenas módulos padrões do Python.

---

## 7. Restrições

- O sistema não possui interface gráfica.  
- Não possui múltiplos usuários ou autenticação.  
- Armazenamento limitado ao arquivo local.

---