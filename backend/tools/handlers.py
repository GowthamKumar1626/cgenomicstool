import pandas as pd

def validate_data(request):
    
    
    if request.data["genome_column_name"] == "":
        raise ValueError("Genome column value required")
    else:
        genome_column = request.data["genome_column_name"]
        
    if request.data["gene_column_name"] == "":
        raise ValueError("Gene column value required")
    else: 
        gene_column = request.data["gene_column_name"]
        
    if request.data["data_format"] == "":
        raise ValueError("Select a value either CGE or PATRIC")
    else:
        data_format = request.data["data_format"]
        
    try:
        chop_genome_name_at = request.data["chop_genome_name_at"]
    except Exception as e:
        chop_genome_name_at = ""
        print(f"chop_genome_name_at Set to null: {e}")
        
    dataset = request.FILES['dataset']
    
    try:
        phylo_path = request.FILES['phylo_path']
    except Exception as e:
        phylo_path = ""
        print(f"Path set to null: {e}")
        
    return {
            "genome_column_name": genome_column,
            "gene_column_name": gene_column,
            "chop_genome_name_at":chop_genome_name_at,
            "data_format": data_format,
            "upload_dataset": dataset,
            "phylo_path": phylo_path,
        }
        
def extract_column_names(file):
    return list(pd.read_csv(file))