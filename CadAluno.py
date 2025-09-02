# lista para armazenar os alunos cadastrados
alunos = []
# loop principal do programa
while True:
    # exibe o menu de opções
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # cadastra aluno
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        idade = input("Digite a idade do aluno: ")
        # cria O dicionário para armazenar
        aluno = {
            "nome": nome,
            "matricula": matricula,
            "idade": idade
        }
        # adiciona o alumo à lista
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
    elif opcao == "2":
        # listS alunos cadastrados
        print("\nLista de alunos cadastrados:")
        if not alunos: 
            # verifica se tem alguem ma lista
            print("Nenhum aluno cadastrado.")
        else:
            # exibe os alunos cadastrados, se tiver
            for i, aluno in enumerate(alunos, 1): 
                # enumera a lista para mostrar o número do aluno
                print(f"{i}. Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}")
                # acess dados do aluno pelo dicionário
    elif opcao == "3": 
        # sair
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
