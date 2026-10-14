"""TaskTracker - Fase 2 (Bootcamp II)

Aplicação CLI para cadastrar e visualizar tarefas.
Autor: Fábio Roberto Queiroz Costa Júnior - RA 22551751
"""

# Lista que guarda todas as tarefas (cada tarefa é um dicionário)
tarefas = []

# Prioridades aceitas (chave em minúsculo -> valor padronizado)
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def ler_titulo():
    """Pede o título até o usuário digitar algo válido (não vazio)."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def ler_prioridade():
    """Pede a prioridade até o usuário digitar Alta, Média/Media ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa():
    """Coleta os dados, valida e salva uma nova tarefa na lista."""
    print("\n--- Cadastrar nova tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (ex: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "status": "Pendente",  # status automático no cadastro
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    """Exibe todas as tarefas ou avisa que a lista está vazia."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título     : {tarefa['titulo']}")
        print(f"  Descrição  : {tarefa['descricao']}")
        print(f"  Prioridade : {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite']}")
        print(f"  Status     : {tarefa['status']}")


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    """Loop principal do menu."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Saindo do TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
