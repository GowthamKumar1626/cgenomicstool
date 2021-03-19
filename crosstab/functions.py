import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CrossTab:
    def __init__(self, filepath):
        self.filepath = filepath
    def prepare_dataset(self):
        self.dataframe = pd.read_csv(self.filepath)
        self.dataframe = pd.concat([self.dataframe["Genome"], self.dataframe["Gene"]], axis=1)
        self.dataframe = self.dataframe.dropna(axis=0)
        self.dataframe = self.dataframe.drop_duplicates()
    def corsstab(self):
        self.corsstab = pd.crosstab(self.dataframe["Genome"], self.dataframe["Gene"])
        # self.corsstab.to_csv("./static/files/crosstab.csv")
        self.corsstab.to_csv("./cgenomicstool/static/files/crosstab.csv")
    def heatmap(self):
        values = self.corsstab.iloc[:, :].values
        plt.switch_backend("AGG")
        plt.figure(figsize=(10,8))
        sns.heatmap(values, vmin=0, vmax=1, cmap="YlGnBu")
        plt.xlabel("Genes on X axis")
        plt.ylabel("Genome on y axis")
        # plt.savefig("./static/img/crosstab.png", bbox_inches = 'tight')
        plt.savefig("./cgenomicstool/static/img/crosstab.png", bbox_inches = 'tight')


class GeneAndGenome:
    def read_crosstab(self):
        corsstab_dataframe = pd.read_csv("./cgenomicstool/static/files/crosstab.csv")
        self.crosstab_gene = list(corsstab_dataframe)[1:]
        self.crosstab_genome = list(corsstab_dataframe["Genome"])
        values = corsstab_dataframe.iloc[:, 1:].values
        self.values = values.T
    def crosstab_gene_vs_genome(self):
        def gene_name_filter(value):
            if value[0] == 0:
                return False
            else:
                return value
        genome_present = []
        for i in range(len(self.crosstab_gene)):
            result = list(filter(gene_name_filter, list(zip(self.values[i], self.crosstab_genome))))
            genome_present.append([each[1] for each in result])
        
        self.gene_vs_genome = list(zip(self.crosstab_gene, genome_present))
    def get_data(self):
        return (self.crosstab_gene, self.crosstab_genome, self.gene_vs_genome)