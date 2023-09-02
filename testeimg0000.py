# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:05:35 2023

@author: jterr
"""

import csv
import pylidc as pl
import glob
import fiftyone as fo
import pydicom
import numpy as np
from PIL import Image
import zlib
annotations ={}
image_annotations = []
dataset = fo.Dataset("dataset_T1T2_treino76")
#print(ann[aux].)
# Persist the dataset on disk in order to 
# be able to load it in one line in the future
dataset.persistent = True
# Add your samples to the dataset
path_img="C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/dataHC/lesoes-T1-T2/001/dicomRT/Original-dcm/IMG0000.jpg"
try:
    background_mask =Image.open(path_img)
    seg2=np.array(background_mask, dtype=np.uint8)
    image_annotations.append({
                "bbox": [300,123,111, 321],
                "seg" : seg2,
                "label": "non-nodule",
            })
    annotations[path_img] = image_annotations
     
            # Convert detections to FiftyOne format
    detections = []
    for obj in annotations[path_img]:
            label = obj["label"]
        
            # Bounding box coordinates should be relative values
            # in [0, 1] in the following format:
            # [top-left-x, top-left-y, width, height]
            bounding_box = obj["bbox"]
            
            segmentation=obj["seg"]
            detections.append(
                fo.Detection(label=label, bounding_box=bounding_box, mask=segmentation)
            )
    sample = fo.Sample(path_img)      
        # Store detections in a field name of your choice
    sample["ground_truth"] = fo.Detections(detections=detections)
        
    dataset.add_sample(sample)
        
    export_dir = "C:/Users/jterr/Documents/Projeto_IC/GRCNN/base_dados_HC/datasetT1_T2_train_teste"
    label_field = "ground_truth"  # for example
    
    # Export the dataset
    dataset.export(
     export_dir=export_dir,
     dataset_type=fo.types.COCODetectionDataset,
     label_field=label_field,
     )
    dataset = fo.Dataset.from_dir(dataset_dir=export_dir, dataset_type=fo.types.COCODetectionDataset )
except Exception as e:
    print("An error occurred:", e)
