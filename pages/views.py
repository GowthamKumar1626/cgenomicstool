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
    request.session["job_id"] = job_id

    result = ResultModel.objects.get(job_id=job_id)
    image_path = "/media/"+str(result.image)

    record = IPAddressModel.objects.get(job_id=job_id)
    
    dataset = pd.read_csv(result.data)
    crosstab_gene = list(dataset)[1:]
    crosstab_genome = list(dataset["Genome"])
    values = dataset.iloc[:, 1:].values
    values = values.T

    gene_genome_lengths = []
    for i in range(len(values)):
        gene_genome_lengths.append(len(np.where(values[i]==1)[0]))
    genome_length_wrt_gene = list(zip(crosstab_gene, gene_genome_lengths))

    filled_form = UploadFileForm()
    file_recieved_note = "Successfully file recieved"

    return render(request, "pages/result_overview.html", {
                "form": filled_form,
                "filled_form_note": file_recieved_note,
                "record": record,
                "image": image_path,
                "gene": crosstab_gene,
                "genome": crosstab_genome,
                "genome_length_wrt_gene": genome_length_wrt_gene, 
                "crosstab_download": result.data,
                "encodings_download": result.encodings,
    })

# genome_info - /tools/crosstab/<gene_name>
def genome_info(request, job_id, gene_name):
    # Getting job_id from SESSION variable
    record = IPAddressModel.objects.get(job_id=job_id)
    result = ResultModel.objects.get(job_id=job_id)
    image_path = "/media/"+str(result.image)
    
    crosstab_gene, crosstab_genome, values = GeneAndGenomeHandler()
    index = crosstab_gene.index(gene_name)
    gene_genome_names = [crosstab_genome[pos] for pos in np.where(values[index]==1)[0]]
    genomes_wrt_gene = list(zip(np.where(values[index]==1)[0], gene_genome_names))

    gene_genome_lengths = []
    for i in range(len(values)):
        gene_genome_lengths.append(len(np.where(values[i]==1)[0]))
    genome_length_wrt_gene = list(zip(crosstab_gene, gene_genome_lengths))

    file_recieved_note = "Successfully file recieved"
    newForm = UploadFileForm()

    return render(request, "pages/result_overview.html", {
            "form": newForm,
            "filled_form_note": file_recieved_note,
            "record": record,
            "image": image_path,
            "gene": crosstab_gene,
            "genome": crosstab_genome,
            "genome_length_wrt_gene": genome_length_wrt_gene,
            "gene_name": gene_name,
            "genomes_wrt_gene": genomes_wrt_gene,
            "crosstab_download": result.data,
            "encodings_download": result.encodings,
        })


def delete_job(request, job_id):
    IPAddressModel.objects.filter(job_id=job_id).delete()
    return render(request, "pages/results.html")