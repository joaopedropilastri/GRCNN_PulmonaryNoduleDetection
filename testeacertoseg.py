# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:46:12 2023

@author: jterr
"""

import json

# Caminho para o arquivo JSON
json_file = "C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/datasetT1_T2_test/labels.json"

# Carregar o JSON
with open(json_file, "r") as file:
    data = json.load(file)

# Percorrer as anotações e substituir segmentações vazias
for annotation in data["annotations"]:
    if not annotation["segmentation"]:
        annotation["segmentation"] = [[0, 0, 0, 512, 512, 512, 512, 0]]

# Salvar as alterações de volta no arquivo JSON
with open(json_file, "w") as file:
    json.dump(data, file, indent=4)  # O indent=4 é opcional, mas formata o JSON para ser mais legível
