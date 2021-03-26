from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from crosstab.handlers import GeneAndGenomeHandler
from crosstab.models import IPAddressModel, ResultModel
from crosstab.form import UploadFileForm

import pandas as pd
import numpy as np

def index(request):
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")

def results(request):
    return render(request, "pages/results.html", {
        "results": IPAddressModel.objects.all()
    })

def job_details(request, job_id):
    result = ResultModel.objects.get(job_id=job_id)
    image_path = "/media/"+str(result.image)
    
    dataset = pd.read_csv(result.data)
    crosstab_gene = list(dataset)[1:]
    crosstab_genome = list(dataset["Genome"])
    values = dataset.iloc[:, 1:].values
    values = values.T
    filled_form = UploadFileForm()
    file_recieved_note = "Successfully file recieved"

    return render(request, "pages/result_overview.html", {
                "form": filled_form,
                "filled_form_note": file_recieved_note,
                "image": image_path,
                "gene": crosstab_gene,
                "genome": crosstab_genome,
    })

# genome_info - /tools/crosstab/<gene_name>
def genome_info(request, job_id, gene_name):
    # Getting job_id from SESSION variable
    result = ResultModel.objects.get(job_id=job_id)
    image_path = "/media/"+str(result.image)
    
    crosstab_gene, crosstab_genome, values = GeneAndGenomeHandler()
    index = crosstab_gene.index(gene_name)
    gene_genome_names = [crosstab_genome[pos] for pos in np.where(values[index]==1)[0]]
    genomes_wrt_gene = list(zip(np.where(values[index]==1)[0], gene_genome_names))
    file_recieved_note = "Successfully file recieved"
    newForm = UploadFileForm()

    return render(request, "pages/result_overview.html", {
            "form": newForm,
            "filled_form_note": file_recieved_note,
            "image": image_path,
            "gene": crosstab_gene,
            "genome": crosstab_genome,
            "gene_name": gene_name,
            "genomes_wrt_gene": genomes_wrt_gene,
        })


def delete_job(request, job_id):
    IPAddressModel.objects.filter(job_id=job_id).delete()
    return render(request, "pages/results.html")