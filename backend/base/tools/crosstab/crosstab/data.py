from pandas.core.frame import DataFrame
from pandas.core.reshape.pivot import crosstab
from crosstab.handlers import try_except
from crosstab.Exceptions import *
from crosstab.io import save_dataset
from crosstab.meta_data import encode, load_meta_data

import numpy as np
import pandas as pd
import pandas
from typing import TypeVar
import os

@try_except
def generate_crosstab(
        dataset: pandas.core.frame, 
        col_1="Genome Name"
    ) -> pandas.core.frame :
    
    columns = dataset.columns.tolist()

    if col_1 not in columns:
        msg = f"{col_1} column is not present in dataset"
        raise ValueError(msg)
    col_2 = [col for col in columns if col != col_1][0]
    dataset = crosstab(dataset[col_1], dataset[col_2])

    return dataset






