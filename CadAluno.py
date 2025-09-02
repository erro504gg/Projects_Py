alunos = []

while True:
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        idade = input("Digite a idade do aluno: ")
        aluno = {
            "nome": nome,
            "matricula": matricula,
            "idade": idade
        }
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    elif opcao == "2":
        print("\nLista de alunos cadastrados:")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for i, aluno in enumerate(alunos, 1):
                print(f"{i}. Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")