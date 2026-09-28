clientes = []


def cadastrar_cliente():
    nome = input("Nome do cliente: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return

    email = input("E-mail do cliente: ").strip()
    telefone = input("Telefone do cliente: ").strip()

    clientes.append({"nome": nome, "email": email, "telefone": telefone})
    print("Cliente cadastrado com sucesso!")


def pesquisar_cliente():
    nome_pesquisado = input("Nome para pesquisa: ").strip().casefold()
    encontrados = [cliente for cliente in clientes
                   if nome_pesquisado in cliente["nome"].casefold()]

    if encontrados:
        print("Clientes encontrados:")
        for cliente in encontrados:
            print(f"- Nome: {cliente['nome']}")
            print(f"  E-mail: {cliente['email']}")
            print(f"  Telefone: {cliente['telefone']}")
    else:
        print("Nenhum cliente encontrado.")


def listar_clientes():
    if not clientes:
        print("Não há clientes cadastrados.")
        return

    print("Clientes cadastrados:")
    for cliente in clientes:
        print(f"- Nome: {cliente['nome']}")
        print(f"  E-mail: {cliente['email']}")
        print(f"  Telefone: {cliente['telefone']}")


while True:
    print("\n--- Sistema de Cadastro de Clientes ---")
    print("1. Cadastrar cliente")
    print("2. Pesquisar cliente pelo nome")
    print("3. Listar todos os clientes")
    print("4. Encerrar o programa")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        pesquisar_cliente()
    elif opcao == "3":
        listar_clientes()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")