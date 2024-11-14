import json
import csv
import os
 
# Definir o diretório dos arquivos JSON de entrada e o caminho para o CSV de saída
json_dir_path = '##'  # Diretório contendo os arquivos JSON
csv_file_path = '##'  # Caminho do arquivo CSV de saída
 
# "doc" de cada JSON em uma lista
all_docs = []
fieldnames = set()
 
#JSON no diretório
for json_filename in os.listdir(json_dir_path):
    if json_filename.endswith('.json'):
        json_file_path = os.path.join(json_dir_path, json_filename)
        # Ler JSON
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        # Extrair apenas os dados da lista de objetos "doc" dentro de "rows"
        docs = [item['doc'] for item in data['rows'] if 'doc' in item]
        all_docs.extend(docs)  # Agregar os docs no total
        # Atualizar o conjunto de chaves para o cabeçalho do CSV
        for doc in docs:
            fieldnames.update(doc.keys())
 
# Converter lista para manter compatibilidade com DictWriter
fieldnames = list(fieldnames)
 
# Escrever no arquivo CSV
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()  # Escrever o cabeçalho no CSV
    writer.writerows(all_docs)  # Escrever todos os dados agregados
 
print("Conversão concluída. O arquivo CSV foi salvo como:", csv_file_path)
