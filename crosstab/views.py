# Imports
from django.shortcuts import render
from .form import UploadFileForm
from .models import IPAddressModel
from .handlers import CrossTabHandler, GeneAndGenomeHandler

import numpy as np

# View functions
# index - /tools/crosstab/
def index(request):
    ip_address = request.META["REMOTE_ADDR"]
    file_recieved_note = None
    if request.method == 'POST':                                                    # Checking for post method
        filled_form = UploadFileForm(request.POST, request.FILES)                   # Getting filled form details
        if filled_form.is_valid():                                                  # Validating filled form
            file_recieved_note = "Successfully file recieved"                       # Success Note
            CrossTabHandler(filled_form.cleaned_data["file"])                       # Sending uploaded filepath to Hnadler
            crosstab_gene, crosstab_genome, values = GeneAndGenomeHandler()         # Getting gene, genome data

            # Record creation in database
            IPAddressModel.objects.create(ip_address=ip_address)

            #Rendering HTTP content for POST request
            return render(request, 'crosstab/index.html', {
                "form": filled_form,
                "filled_form_note": file_recieved_note,
                "gene": crosstab_gene,
                "genome": crosstab_genome,
            })
    else:
        empty_form = UploadFileForm()
        return render(request, 'crosstab/index.html', {
            'form': empty_form
        })

# genome_info - /tools/crosstab/<gene_name>
def genome_info(request, gene_name):
    crosstab_gene, crosstab_genome, values = GeneAndGenomeHandler()
    index = crosstab_gene.index(gene_name)
    gene_genome_names = [crosstab_genome[pos] for pos in np.where(values[index]==1)[0]]
    genomes_wrt_gene = list(zip(np.where(values[index]==1)[0], gene_genome_names))
    file_recieved_note = "Successfully file recieved"
    newForm = UploadFileForm()
    return render(request, "crosstab/index.html", {
            "form": newForm,
            "filled_form_note": file_recieved_note,
            "gene": crosstab_gene,
            "genome": crosstab_genome,
            "gene_name": gene_name,
            "genomes_wrt_gene": genomes_wrt_gene,
        })

# about - /tools/crosstab/about/
def about(request):
    return render(request, 'crosstab/about.html')


