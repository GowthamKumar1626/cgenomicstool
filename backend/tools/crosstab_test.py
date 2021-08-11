import pandas as pd
from tools.crosstab.plots import plot, plot_chunks, plot_range
from tools.crosstab.io import load_dataset, save_dataset, read_phylo
from tools.crosstab.preprocessing import cge_to_patric, extract_columns, categorization, reorder_dataset
from tools.crosstab.data import generate_crosstab
from tools.crosstab.zip_files import zip_files

import ssl
import datetime
ssl._create_default_https_context = ssl._create_unverified_context


def result_id_generator():
# file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"result-id-{datetime.datetime.now()}"


def load_params(data, user_id):
    
    try: 
        genome_column = data["genome_column_name"]
        gene_column = data["gene_column_name"]
        data_format = data["data_format"]
        chop_genome_name_at = data["chop_genome_name_at"]
        # phylo_path = "./datasets/phylo.newick"
        if data["phylo_path"] == "null" or data["phylo_path"] == "":
            data["phylo_path"] = None
        
        phylo_path = data["phylo_path"]

        dataset = load_dataset(data["upload_dataset"])
        
    except Exception as error:
        print("Error in params", error)
         
    dataset = extract_columns(dataset, chop_genome_name_at, genome_column, gene_column)
    if data_format.lower() == "cge":
        dataset = cge_to_patric(dataset)
    
    crosstab = generate_crosstab(dataset, col_1=genome_column)
    
    if phylo_path != None:
        print("Phylo Path Given")
        genome_order = read_phylo(phylo_path)
        crosstab = reorder_dataset(crosstab, genome_order, genome_column)
    
    result_stamp = result_id_generator()
    print(result_stamp)
    file_path = f"./static/files/{result_stamp}.csv"
    image_path = f"./static/images/{result_stamp}.jpeg"
    save_dataset(crosstab, file_path)
    # crosstab_json = pd.read_csv(file_path).to_html() 
    dataset = crosstab.copy()
    
    plot(dataset, image_path)
    # plot_chunks(crosstab, n_gene_per_plot=30)
    
    # zip_files("./static/results")
    # shutil.rmtree("./static/results/")
    print("Filepath saved")
    
    return result_stamp

