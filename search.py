def ler_arquivo_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def buscar_dados_por_nome(dados, nome_pessoa):
    nome_pessoa_normalizado = nome_pessoa.strip().lower() 
    for pessoa in dados['pessoas']: 
        dados_pessoais = pessoa.get('dados_pessoais', {})
        nome_pessoa_no_json = dados_pessoais.get('nome_civil', '').strip().lower()

        if nome_pessoa_normalizado == nome_pessoa_no_json:
            cpf = dados_pessoais.get('cpf', 'CPF não encontrado')

            registro_coren = 'Não encontrado'
            data_inscricao = 'Não encontrada'

            for categoria in pessoa.get('categorias', []):
                numero_registro = categoria.get('numero_registro', 'Não encontrado')
                data_registro = categoria.get('data_registro', 'Não encontrada')

                for inscricao in categoria.get('inscricoes', []):
                    if inscricao.get('inscricao_atual', False):
                        registro_coren = numero_registro
                        data_inscricao = inscricao.get('data_inscricao', 'Não encontrada')

            return cpf, registro_coren, data_inscricao

    return 'Pessoa não encontrada', '', ''

caminho_arquivo = 'MigCorenProf_MG_20231211-153529.json' 

nomes_pessoas = [
         "Adicionar o nome das pessoas assim",
         "Andreia Aparecida de Lima"

]

dados = ler_arquivo_json(caminho_arquivo)

if dados:
    for nome in nomes_pessoas:
        cpf, registro_coren, data_inscricao = buscar_dados_por_nome(dados, nome)
        print(f"Nome: {nome}, CPF: {cpf}, Reg. COREN-MG: {registro_coren}, Data de Inscrição: {data_inscricao}")
else:
    print("Não foi possível carregar os dados do arquivo.")
