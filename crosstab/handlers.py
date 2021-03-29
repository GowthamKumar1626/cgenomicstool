from .functions import CrossTab, GeneAndGenome
from datetime import datetime
import numpy as np

class CrossTabHandler:
    def __init__(self, filename):
        CT = CrossTab(filename)
        CT.prepare_dataset()
        CT.corsstab()
        CT.heatmap()

class GeneAndGenomeHandler:
    def __new__(cls):
        GG = GeneAndGenome()
        GG.read_crosstab()
        GG.encodings()
        return GG.get_data()

def encodings(crosstab_gene, values):
    gene_genome_lengths = []
    for i in range(len(values)):
        gene_genome_lengths.append(len(np.where(values[i]==1)[0]))
    return list(zip(crosstab_gene, gene_genome_lengths))


def genereate_id():
    return "crosstab-R"+datetime.now().strftime("%Y%m%d-%H%M%S-")+str(datetime.now().timestamp()).replace('.', '-')


def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M%S-")+str(now.timestamp()).replace('.', '-')

    if extension == "png":
        return 'images/%s.%s' % (f"crosstab_image_{timestamp}", extension)
    elif extension == "json":
        return 'files/%s.%s' % (f"crosstab_result_data_{timestamp}", extension)
    return 'uploads/%s.%s' % (f"crosstab_files_{timestamp}", extension)