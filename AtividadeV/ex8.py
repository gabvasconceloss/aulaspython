def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    else:
        print("A tarefa não pode ficar vazia.")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nTarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            print(f'Tarefa "{removida}" removida com sucesso!')
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Digite um número válido.")


def main():
    tarefas = []

    while True:
        print("\n--- Menu de Tarefas ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            remover_tarefa(tarefas)
        elif opcao == "4":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


if __name__ == "__main__":
    main()