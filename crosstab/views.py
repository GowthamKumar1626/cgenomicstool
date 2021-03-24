from django.shortcuts import render
from .form import UploadFileForm
from .handlers import CrossTabHandler, GeneAndGenomeHandler

def index(request):
    ip_address = request.META["REMOTE_ADDR"]
    if request.method == 'POST':
        filled_form = UploadFileForm(request.POST, request.FILES)
        if filled_form.is_valid():
            file_recieved_note = "Successfully file recieved"
            CrossTabHandler(filled_form.cleaned_data["file"])
            crosstab_gene, crosstab_genome, crosstab_gene_vs_genome = GeneAndGenomeHandler()
            return render(request, 'crosstab/index.html', {
                "form": filled_form,
                "filled_form_note": file_recieved_note,
                "gene": crosstab_gene,
                "genome": crosstab_genome,
                "gene_vs_genome": crosstab_gene_vs_genome
            })
    else:
        empty_form = UploadFileForm()
        return render(request, 'crosstab/index.html', {
            'form': empty_form
        })

def genome_info(request, gene_name):
    crosstab_gene, crosstab_genome, crosstab_gene_vs_genome = GeneAndGenomeHandler()
    index = crosstab_gene.index(gene_name)
    gene_genome_names = crosstab_gene_vs_genome[index][1]
    file_recieved_note = "Successfully file recieved"
    newForm = UploadFileForm()
    return render(request, "crosstab/index.html", {
            "form": newForm,
            "filled_form_note": file_recieved_note,
            "gene": crosstab_gene,
            "gene_name": gene_name,
            "genome": crosstab_genome,
            "gene_vs_genome": crosstab_gene_vs_genome,
            "genomes_wrt_gene": gene_genome_names,
        })

def about(request):
    return render(request, 'crosstab/about.html')


