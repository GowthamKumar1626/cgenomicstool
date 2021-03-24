from django import template
from crosstab.handlers import GeneAndGenomeHandler

crosstab_gene, crosstab_genome, crosstab_gene_vs_genome = GeneAndGenomeHandler()

register = template.Library()

@register.filter
def index_of(value):
    index = crosstab_genome.index(value)
    return index