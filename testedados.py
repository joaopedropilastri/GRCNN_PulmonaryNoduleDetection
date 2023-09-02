# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 11:12:55 2023

@author: jterr
"""

import json

def verify_coco_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    if "images" not in data or "annotations" not in data:
        print("Arquivo JSON inválido. Chaves 'images' e 'annotations' são obrigatórias.")
        return False

    images = data["images"]
    annotations = data["annotations"]
    existing_image_ids = set(image["id"] for image in images)
    existing_category_ids = set(annotation["category_id"] for annotation in annotations)

    for image in images:
        # Verificar chaves obrigatórias em cada objeto 'image'
        if "id" not in image or "file_name" not in image or "height" not in image or "width" not in image:
            print("Objeto 'image' inválido. Chaves obrigatórias ausentes.")
            return False

        # Verificar valores numéricos esperados
        if not isinstance(image["id"], int) or image["id"] <= 0:
            print("Valor inválido para 'id' em um objeto 'image'. Deve ser um inteiro positivo.")
            return False

        if not isinstance(image["height"], int) or image["height"] <= 0:
            print("Valor inválido para 'height' em um objeto 'image'. Deve ser um inteiro positivo.")
            return False

        if not isinstance(image["width"], int) or image["width"] <= 0:
            print("Valor inválido para 'width' em um objeto 'image'. Deve ser um inteiro positivo.")
            return False

    for annotation in annotations:
        # Verificar chaves obrigatórias em cada objeto 'annotation'
        if "id" not in annotation or "image_id" not in annotation or "category_id" not in annotation \
                or "bbox" not in annotation or "segmentation" not in annotation \
                or "area" not in annotation or "iscrowd" not in annotation:
            print("Objeto 'annotation' inválido. Chaves obrigatórias ausentes.")
            return False

        # Verificar valores numéricos esperados
        if not isinstance(annotation["id"], int) or annotation["id"] <= 0:
            print("Valor inválido para 'id' em um objeto 'annotation'. Deve ser um inteiro positivo.")
            return False

        if not isinstance(annotation["image_id"], int) or annotation["image_id"] <= 0:
            print("Valor inválido para 'image_id' em um objeto 'annotation'. Deve ser um inteiro positivo.")
            return False

        if not isinstance(annotation["category_id"], int) or annotation["category_id"] not in existing_category_ids:
            print("Valor inválido para 'category_id' em um objeto 'annotation'. Deve ser um ID válido de categoria.")
            return False

        if not isinstance(annotation["area"], (int, float)) or annotation["area"] <= 0:
            print("Valor inválido para 'area' em um objeto 'annotation'. Deve ser um número positivo.")
            return False

        if not isinstance(annotation["iscrowd"], int) or annotation["iscrowd"] not in (0, 1):
            print("Valor inválido para 'iscrowd' em um objeto 'annotation'. Deve ser 0 ou 1.")
            return False

        # Verificar estrutura das chaves 'bbox' e 'segmentation'
        if not isinstance(annotation["bbox"], list) or len(annotation["bbox"]) != 4:
            print("Valor inválido para 'bbox' em um objeto 'annotation'. Deve ser uma lista de comprimento 4.")
            return False

        if not isinstance(annotation["segmentation"], list) or not all(isinstance(seg, list) for seg in annotation["segmentation"]):
            print("Valor inválido para 'segmentation' em um objeto 'annotation'. Deve ser uma lista de listas.")
            return False

    return True

# Exemplo de uso
json_file = "C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/datasetT1_T2_train4/labels.json"
if verify_coco_data(json_file):
    print("Dados COCO format válidos.")
else:
    print("Dados COCO format inválidos.")
