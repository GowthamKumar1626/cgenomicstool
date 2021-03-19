from .functions import CrossTab, GeneAndGenome


class CrossTabHandler:
    def __init__(self, filename):
        CT = CrossTab(filename)
        CT.prepare_dataset()
        CT.corsstab()
        CT.heatmap()

class GeneAndGenomeHandler:
    # def __init__(self):
    #     GG = GeneAndGenome()
    #     GG.read_crosstab()
    #     GG.crosstab_gene_vs_genome()
    #     self.crosstab_gene, self.crosstab_genome, self.crosstab_gene_vs_genome = GG.get_data()
    def __new__(cls):
        GG = GeneAndGenome()
        GG.read_crosstab()
        GG.crosstab_gene_vs_genome()
        return GG.get_data()


# self.crosstab_gene, self.crosstab_genome, self.crosstab_gene_vs_genome = 