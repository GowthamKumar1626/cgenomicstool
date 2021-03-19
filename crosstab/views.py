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

def about(request):
    return render(request, 'crosstab/about.html')


