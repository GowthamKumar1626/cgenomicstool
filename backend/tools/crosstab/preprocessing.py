"""
This module includes all the methods required for preprocssing dataset provided by user
"""
from tools.crosstab.Exceptions import *
from tools.crosstab.handlers import *
from tools.crosstab.meta_data import *

import pandas as pd
import pandas
import os

@try_except
def cge_to_patric(dataset):
    return dataset.apply(lambda each_gene: each_gene.str.split(',').explode()).reset_index().drop("index", axis=1)

@try_except
def extract_columns(dataset, chop_genome_name_at = "strain", col_1 =  "Genome Name", col_2 = "Gene"):

    col_1_valid = col_1 in dataset.columns
    assert col_1_valid, f"column '{col_1}' is not found in dataset"

    col_2_valid = col_2 in dataset.columns
    assert col_2_valid, f"column '{col_2}' is not found in dataset"

    dataset = pd.concat([dataset[col_1], dataset[col_2]], axis=1)
    dataset = dataset.dropna(axis=0)
    dataset = dataset.drop_duplicates()

    # Converting CGE format to PATRIC Format
    # if data_format.lower() == "cge":
    #     dataset = cge_to_patric(dataset)
    dataset[col_1] = dataset[col_1].apply(lambda x: x.split(chop_genome_name_at)[-1])

    return dataset

@try_except
def categorization(dataset):
    _, meta_genes, class_encodings  = load_meta_data()
    encodings_present = []

    for col in dataset.keys():
        gene = str(col).split("-")[0].lower().replace(" ", "")
        encoding = encode(gene, class_encodings, meta_genes)
        dataset[col] = dataset[col].map({1: encoding, 0: 0})
        encodings_present.append(encoding)
        
    return (dataset, encodings_present)

def reorder_dataset(
    dataset: pandas.core.frame,
    genome_order: list, 
    col: str
    ) -> pandas.core.frame:
    
    dataset = pd.DataFrame(dataset.to_records()).set_index(col)      # Converting pivot to pandas dataframe and setting Genome as index
    genome_list = [each[1:] for each in sorted(dataset.index.tolist())]
    dataset.index = genome_list
    if genome_list == sorted(genome_order):                  # Check elements in crosstab and genome order same or not
        dataset = dataset.reindex(genome_order)
        print("Reindexed Successfully")

    return dataset

@try_except
def divide_chunks(l, n):

    for i in range(0, len(l), n):
        yield l[i:i + n]

