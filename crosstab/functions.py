import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

class CrossTab:
    def __init__(self, filepath):
        self.filepath = filepath
    def prepare_dataset(self):
        self.dataframe = pd.read_csv(self.filepath)
        self.dataframe = self.dataframe[["Genome", "Gene"]]
        self.dataframe = (self.dataframe.apply(lambda x: x.str.split(',').explode()).reset_index()).drop("index", axis=1)
        self.dataframe = self.dataframe.dropna(axis=0)
        self.dataframe = self.dataframe.drop_duplicates()
    def corsstab(self):
        self.corsstab = pd.crosstab(self.dataframe["Genome"], self.dataframe["Gene"])
        self.corsstab.to_csv("./cgenomicstool/static/files/crosstab.csv")
    def heatmap(self):
        self.values = self.corsstab.iloc[:, :].values
        plt.switch_backend("AGG")
        plt.figure(figsize=(10,8))
        sns.heatmap(self.values, vmin=0, vmax=1, cmap="YlGnBu")
        plt.xlabel("Genes")
        plt.ylabel("Genomes")
        # plt.savefig("./static/img/crosstab.png", bbox_inches = 'tight')
        plt.savefig("./cgenomicstool/static/img/crosstab.png", bbox_inches = 'tight')


class GeneAndGenome:
    def read_crosstab(self):
        corsstab_dataframe = pd.read_csv("./cgenomicstool/static/files/crosstab.csv")
        self.crosstab_gene = list(corsstab_dataframe)[1:]
        self.crosstab_genome = list(corsstab_dataframe["Genome"])
        values = corsstab_dataframe.iloc[:, 1:].values
        self.values = values.T
    def encodings(self):
        self.genome_encodigs = []
        for i in range(len(self.values)):
            self.genome_encodigs.append("\n".join([f"{i}-{self.crosstab_genome[i]}" for i in np.where(self.values[i]==1)[0]]))
        self.gene_encodings = [f"{i}-{self.crosstab_gene[i]}" for i in range(len(self.crosstab_gene))]
        self.encodings = list(zip(self.gene_encodings, self.genome_encodigs))
        
        with open("./cgenomicstool/static/files/encodings.csv", 'w') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(["Gene", "Genomes"])
            [wr.writerow([gene, genome]) for gene, genome in self.encodings]

        myfile.close()
    def get_data(self):
        return (self.crosstab_gene, self.crosstab_genome, self.values)