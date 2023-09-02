import json
import os

def remove_empty_masks_and_image(json_file, image_dir):
    with open(json_file, 'r') as f:
        data = json.load(f)

    image_ids_to_remove = set()
    image_files_to_remove = set()

    # Encontra os image_ids correspondentes às linhas com máscara vazia
    for item in data['annotations']:
        if not item['segmentation']:
            image_ids_to_remove.add(item['image_id'])

    # Remove as linhas com máscara vazia
    data['annotations'] = [item for item in data['annotations'] if item['image_id'] not in image_ids_to_remove]

    # Remove as linhas correspondentes aos image_ids e imagens com nomes de arquivo correspondentes
    for item in data['images']:
        if item['id'] in image_ids_to_remove:
            image_files_to_remove.add(item['file_name'])

    data['images'] = [item for item in data['images'] if item['id'] not in image_ids_to_remove]

    # Reescreve os IDs de forma ordenada e sequencial
    new_id = 1
    old_to_new_id = {}

    for item in data['annotations']:
        old_id = item['id']
        old_to_new_id[old_id] = new_id
        item['id'] = new_id
        new_id += 1

    for item in data['images']:
        old_id = item['id']
        if old_id in old_to_new_id:
            item['id'] = old_to_new_id[old_id]

    # Remove a imagem com o nome de arquivo correspondente
    for image_file in image_files_to_remove:
        file_path = os.path.join(image_dir, image_file)
        if os.path.exists(file_path):
            os.remove(file_path)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Exemplo de uso
json_file = 'C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/datasetT1_T2_train_sembackmaskteste/labels.json'
image_dir = r'C:\Users\jterr\Documents\Projeto_IC\GRCNN\base_dados_HC\datasetT1_T2_train_sembackmaskteste\data/'
remove_empty_masks_and_image(json_file, image_dir)
