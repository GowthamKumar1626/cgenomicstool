from typing import List
from tools.crosstab.handlers import try_except
from tools.crosstab.Exceptions import *

import pandas as pd
import pandas
from pandas._typing import FilePathOrBuffer
from ete3 import Tree
import os



@try_except
def check_valid_extention(
        extention: str
    ) -> bool :

    valid = False
    if 'csv' in extention:
        valid = True
    elif 'tsv' in extention:
        valid = True
    elif 'xls' in extention:
        valid = True

    return valid

@try_except
def read_dataset(
        path: FilePathOrBuffer, 
        extention: str
    ) -> pandas.core.frame :

    if 'csv' in extention:
        return pd.read_csv(path)
    elif 'tsv' in extention:
        return pd.read_csv(path, sep="\t")
    elif 'xls' in extention:
        return pd.read_excel(path)


@try_except
def load_dataset(
        path: FilePathOrBuffer
    ) -> pandas.core.frame :
    
    extention = os.path.splitext(path)[1]
    valid_extention = check_valid_extention(extention)

    if valid_extention != True:
        msg = f"Invalid file extension {extention}"
        raise InvalidFileFormat(msg)

    dataset = read_dataset(path, extention)
    return dataset

@try_except
def read_phylo(
        path: str
    ) -> List :
        
        """
        Reads a phylogenetic tree in newick format and helps in reordering genomes in dataset.
        
        Args:
            path: phylogenetic file path (newick format) 
            
        Returns:
            genome_order: Contains genome names, ordered according to phylogenetic tree
        
        """
        
        def strip_strains(
                strain: str
            ) -> str :
            if "reference" in strain:
                return None
            return strain.split("/")[0]
        
        """ Reading phylogenetic Tree """
        tree = Tree(path)
        
        """ Extracting Genomic order from phylogenetic tree """
        genome_order = list(map(strip_strains, tree.get_leaf_names()))
        
        if None in genome_order:
            genome_order.remove(None)
            
        return genome_order

@try_except
def save_dataset(
        dataset: pandas.core.frame, 
        path: str
    ) -> None :
    dataset.to_csv(path)