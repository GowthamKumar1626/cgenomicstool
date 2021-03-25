from django.shortcuts import render
from django.http import HttpResponse
from numpy import imag
from crosstab.models import IPAddressModel, ResultModel
from crosstab.form import UploadFileForm
import pandas as pd

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

    return render(request, "crosstab/index.html", {
                "form": filled_form,
                "filled_form_note": file_recieved_note,
                "image": image_path,
                "gene": crosstab_gene,
                "genome": crosstab_genome,
    })