# Lista de estudantes (banco de dados)
estudantes = []

# Função para adicionar um novo estudante
def adicionar_estudante():
    nome = input("Digite o nome do estudante: \n")
    idade = input("Digite a idade do estudante: \n")
    curso = input("Digite o curso do estudante: \n")
    estudante = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }
    estudantes.append(estudante)
    print(f"Estudante {nome} adicionado com sucesso!")

# Função para remover um estudante pelo nome
def remover_estudante():
    nome = input("Digite o nome do estudante a ser removido: \n")
    for estudante in estudantes:
        if estudante["nome"] == nome:
            estudantes.remove(estudante)
            print(f"Estudante {nome} removido com sucesso!")
            return# No caso específico dessa função, quando nenhum estudante é encontrado, não há mais nada a fazer dentro da função, então usamos return para sair imediatamente da função e voltar ao menu principal do programa.
    print(f"Estudante {nome} não encontrado.")

# Função para buscar um estudante pelo nome
def buscar_estudante():
    nome = input("Digite o nome do estudante a ser buscado: \n")
    for estudante in estudantes:
        if estudante["nome"] == nome:
            print(f"Estudante encontrado: Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")
            return # No caso específico dessa função, quando nenhum estudante é encontrado, não há mais nada a fazer dentro da função, então usamos return para sair imediatamente da função e voltar ao menu principal do programa.
    print(f"Estudante {nome} não encontrado.")

# Função para listar todos os estudantes
def listar_estudantes():
    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return # No caso específico dessa função, quando nenhum estudante é encontrado, não há mais nada a fazer dentro da função, então usamos return para sair imediatamente da função e voltar ao menu principal do programa.
    for estudante in estudantes:
        print(f"Nome: {estudante['nome']}, Idade: {estudante['idade']}, Curso: {estudante['curso']}")

# Menu interativo
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar estudante")
        print("2. Remover estudante")
        print("3. Buscar estudante")
        print("4. Listar estudantes")
        print("5. Sair")
        opcao = input("Escolha uma opção: \n")

        if opcao == "1":
            adicionar_estudante()
        elif opcao == "2":
            remover_estudante()
        elif opcao == "3":
            buscar_estudante()
        elif opcao == "4":
            listar_estudantes()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

# Executa o menu
menu()
