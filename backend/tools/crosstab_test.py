import os, shutil
from tools.crosstab.plots import plot, plot_chunks, plot_range
from tools.crosstab.io import load_dataset, save_dataset, read_phylo
from tools.crosstab.preprocessing import cge_to_patric, extract_columns, categorization, reorder_dataset
from tools.crosstab.data import generate_crosstab
from tools.crosstab.zip_files import zip_files

import ssl
import datetime
ssl._create_default_https_context = ssl._create_unverified_context


def load_params(data, user_id):
    
    try: 
        genome_column = data["genome_column_name"]
        gene_column = data["gene_column_name"]
        data_format = data["data_format"]
        chop_genome_name_at = data["chop_genome_name_at"]
        # phylo_path = "./datasets/phylo.newick"
        if data["phylo_path"] == "null":
            data["phylo_path"] = None
        
        phylo_path = data["phylo_path"]

        dataset = load_dataset(data["upload_dataset"])
        
    except:
        print("Error in params")
         
    dataset = extract_columns(dataset, chop_genome_name_at, genome_column, gene_column)
    if data_format.lower() == "cge":
        dataset = cge_to_patric(dataset)

    crosstab = generate_crosstab(dataset, col_1=genome_column)

    if phylo_path != None:
        genome_order = read_phylo(phylo_path)
        crosstab = reorder_dataset(crosstab, genome_order, genome_column)
    
    # if os.path.exists("./static/results"):
    #     shutil.rmtree("./static/results")
    # os.makedirs("./static/results/csv/")
    # os.makedirs("./static/results/images/")
    
    file_path = f"./static/files/crosstab_user_{user_id}_{datetime.datetime.now()}.csv"
    save_dataset(crosstab, file_path)
    # dataset = crosstab.copy()
    
    # plot(dataset)
    # plot_chunks(crosstab, n_gene_per_plot=30)
    
    # zip_files("./static/results")
    # shutil.rmtree("./static/results/")
    
    return file_path

