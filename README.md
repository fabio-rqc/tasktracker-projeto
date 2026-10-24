# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastrar e visualizar tarefas do dia a dia.
Projeto desenvolvido no **Bootcamp II** (Fase 3 – Entrega Final: conteinerização com Docker).

**Autor:** Fábio Roberto Queiroz Costa Júnior – RA 22551751

## Funcionalidades

- Cadastrar nova tarefa (título, descrição, prioridade e data limite)
- Visualizar todas as tarefas cadastradas
- Validação de dados:
  - **Título:** obrigatório; entradas vazias ou só com espaços são rejeitadas
  - **Prioridade:** aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`
- Status definido automaticamente como `Pendente` no cadastro

## Tecnologias

- Python 3.11
- Git e GitHub
- Docker e Docker Compose

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento da Fase 1
├── src/
│   └── main.py                   # Código-fonte da aplicação
├── Dockerfile                    # Receita da imagem Docker
├── docker-compose.yml            # Orquestração da execução interativa
└── README.md
```

## Como executar com Docker

Pré-requisito: ter o [Docker](https://www.docker.com/products/docker-desktop/) instalado e em execução.

Clone o repositório e entre na pasta:

```
git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
cd tasktracker-projeto
```

**Como construir a imagem:**

```
docker build -t tasktracker .
```

**Como rodar o container em modo isolado:**

```
docker run -it tasktracker
```

**Como rodar via orquestração (Recomendado):**

```
docker compose run --rm tasktracker
```

> O parâmetro `-it` (no `docker run`) e as opções `stdin_open` e `tty` (no `docker-compose.yml`)
> são necessários porque a aplicação usa `input()` e precisa de um terminal interativo.

## Como executar sem Docker (opcional)

```
python src/main.py
```

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

## Decisões técnicas

- `python:3.11-slim`: imagem base leve.
- `ENV PYTHONUNBUFFERED=1`: saída do terminal sem atraso (sem buffer).
- `COPY src/ /app/src/`: copia apenas o código-fonte para o container.
- `CMD ["python", "src/main.py"]`: inicia a aplicação ao subir o container.
