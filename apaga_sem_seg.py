import os
import json

# Caminho para o arquivo JSON
json_file = "C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/datasetT1_T2_trainfinal/labels.json"

# Caminho para a pasta que contém as imagens
image_folder = "C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/datasetT1_T2_trainfinal/data/"

# Passo 1: Ler o arquivo JSON
with open(json_file, "r") as file:
    data = json.load(file)
# Obter todos os image_ids existentes nas anotações
existing_image_ids = set(annotation["image_id"] for annotation in data["annotations"])

# Percorrer as imagens
for image in data["images"]:
    image_id = image["id"]
    file_name = image["file_name"]

    # Verificar se o image_id não existe nas anotações
    if image_id not in existing_image_ids:
        # Apagar a imagem correspondente da pasta de dados
        image_path = os.path.join(image_folder, file_name)
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Imagem {file_name} apagada.")
        else:
            print(f"Imagem {file_name} não encontrada.")
