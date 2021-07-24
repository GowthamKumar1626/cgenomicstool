from tools.crosstab.handlers import time_it, try_except

import numpy as np
import pandas as pd


from urllib import request
from io import StringIO


META_DATA_URL = "https://raw.githubusercontent.com/GowthamKumar1626/cgenomicstool/main/backend/static/meta%20data/meta_data.csv"


@try_except
def get_data():
    response = request.urlopen(META_DATA_URL)
    data = response.read()
    text = data.decode('utf-8')
    
    return StringIO(text)

@try_except
def load_meta_data():
    text = get_data()
    dataset = pd.read_csv(text, sep=',')

    class_encodings = dataset["Encodings"].values
    meta_genes = dataset["Gene"].values.tolist()
    gene_class = dataset["Class"].drop_duplicates().tolist()

    return (gene_class, meta_genes, class_encodings)


def encode(
        gene: str, 
        class_encodings: list, 
        meta_genes: list
    ) -> int :
    try:
        index = meta_genes.index(gene)
        return class_encodings[index]
    except ValueError as e:
        return class_encodings.max()+1              # For unknown genes that are not in meta data 
