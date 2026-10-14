# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas do dia a dia.
Projeto desenvolvido no **Bootcamp II** (Fase 2 – Entrega Intermediária).

**Autor:** Fábio Roberto Queiroz Costa Júnior – RA 22551751

## Funcionalidades

- Cadastrar nova tarefa (título, descrição, prioridade e data limite)
- Visualizar todas as tarefas cadastradas
- Validação de dados:
  - **Título:** obrigatório; entradas vazias ou só com espaços são rejeitadas
  - **Prioridade:** aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`
- Status definido automaticamente como `Pendente` no cadastro

## Tecnologias

- Python 3
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Como executar

1. Instale o Python 3 (https://www.python.org/downloads/).
2. Clone o repositório:
   ```
   git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
   cd tasktracker-projeto
   ```
3. Execute:
   ```
   python src/main.py
   ```
   (em Linux/macOS, use `python3 src/main.py`)

## Exemplo de uso

```
===== TASKTRACKER =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
Escolha uma opção: 1
Título da tarefa:
Erro: o título é obrigatório e não pode ficar vazio.
```

## Próximos passos

- Fase 3: empacotamento, containerização com Docker, testes e deploy.
