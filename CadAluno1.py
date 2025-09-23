import datetime

alunos = []
disciplinas = []
notas = []

def calcular_idade(data_nascimento):
    ano_nascimento = int(data_nascimento.split('/')[-1])
    return 2025 - ano_nascimento

def validar_nome(nome):
    return all(parte.isalpha() for parte in nome.split())

def validar_matricula(matricula):
    return matricula.isdigit() and len(matricula) == 12

while True:
    print("\nMenu:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Cadastrar disciplina")
    print("4 - Listar disciplinas")
    print("5 - Cadastrar nota")
    print("6 - Listar notas")
    print("7 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Cadastrar aluno
        while True:
            nome = input("Digite o nome do aluno (somente letras): ").strip()
            if nome and validar_nome(nome):
                break
            print("Nome inválido! Digite apenas letras e não deixe vazio.")

        while True:
            matricula = input("Digite a matrícula do aluno (12 números): ")
            if validar_matricula(matricula):
                break
            print("Matrícula inválida! Digite apenas 12 números.")

        while True:
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            try:
                datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
                idade = calcular_idade(data_nascimento)
                if idade >= 18:
                    break
                else:
                    print("Idade inválida! O aluno deve ter pelo menos 18 anos em 2025.")
            except ValueError:
                print("Data inválida! Use o formato dd/mm/aaaa.")

        aluno = {
            "nome": nome,
            "matricula": matricula,
            "data_nascimento": data_nascimento,
            "idade": idade
        }
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        # Listar alunos cadastrados
        print("\nLista de alunos cadastrados:")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for i, aluno in enumerate(alunos, 1):
                print(f"{i}. Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Idade: {aluno['idade']}")

    elif opcao == "3":
        # Cadastrar disciplina
        nome_disciplina = input("Digite o nome da disciplina: ")
        nome_professor = input("Digite o nome do professor: ")
        turno = input("Digite o turno (Manhã/Tarde/Noite): ")
        sala = input("Digite a sala: ")
        
        disciplina = {
            "nome_disciplina": nome_disciplina,
            "nome_professor": nome_professor,
            "turno": turno,
            "sala": sala
        }
        disciplinas.append(disciplina)
        print("Disciplina cadastrada com sucesso!")

    elif opcao == "4":
        # Listar disciplinas cadastradas
        print("\nLista de disciplinas cadastradas:")
        if not disciplinas:
            print("Nenhuma disciplina cadastrada.")
        else:
            for i, disciplina in enumerate(disciplinas, 1):
                print(f"{i}. Disciplina: {disciplina['nome_disciplina']}, Professor: {disciplina['nome_professor']}, Turno: {disciplina['turno']}, Sala: {disciplina['sala']}")

    elif opcao == "5":
        # Cadastrar nota
        if not alunos or not disciplinas:
            print("Cadastre pelo menos um aluno e uma disciplina antes de lançar notas.")
            continue

        print("\nAlunos:")
        for i, aluno in enumerate(alunos, 1):
            print(f"{i}. {aluno['nome']} (Matrícula: {aluno['matricula']})")
        
        aluno_idx = int(input("Escolha o número do aluno: ")) - 1

        print("\nDisciplinas:")
        for i, disciplina in enumerate(disciplinas, 1):
            print(f"{i}. {disciplina['nome_disciplina']}")
        
        disciplina_idx = int(input("Escolha o número da disciplina: ")) - 1
        
        aluno_nome = alunos[aluno_idx]['nome']
        aluno_matricula = alunos[aluno_idx]['matricula']
        disciplina_nome = disciplinas[disciplina_idx]['nome_disciplina']

        # Verifica se já existe nota para esse aluno e disciplina
        nota_existente = None
        for registro in notas:
            if registro['matricula'] == aluno_matricula and registro['disciplina'] == disciplina_nome:
                nota_existente = registro
                break

        def pedir_nota():
            while True:
                try:
                    nota = float(input("Digite a nota: "))
                    if 0 <= nota <= 10:
                        return nota
                    else:
                        print("Nota inválida! Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Nota inválida! Digite um valor numérico.")

        if nota_existente:
            print(f"Já existe uma nota cadastrada para o aluno '{aluno_nome}' na disciplina '{disciplina_nome}'.")
            alterar = input("Deseja alterar a nota? (s/n): ").strip().lower()
            if alterar == 's':
                nova_nota = pedir_nota()
                nota_existente['nota'] = nova_nota
                print("Nota alterada com sucesso!")
            else:
                print("Nota não alterada.")
        else:
            nota = pedir_nota()
            notas.append({
                "aluno": aluno_nome,
                "matricula": aluno_matricula,
                "disciplina": disciplina_nome,
                "nota": nota
            })
            print("Nota cadastrada com sucesso!")

    elif opcao == "6":
        # Listar notas cadastradas
        print("\nNotas cadastradas:")
        if not notas:
            print("Nenhuma nota cadastrada.")
        else:
            for i, registro in enumerate(notas, 1):
                status = "Aprovado" if registro['nota'] > 5.9 else "Reprovado"
                print(f"{i}. Aluno: {registro['aluno']} (Matrícula: {registro['matricula']}), Disciplina: {registro['disciplina']}, Nota: {registro['nota']} - {status}")

    elif opcao == "7":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
