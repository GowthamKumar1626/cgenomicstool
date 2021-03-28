# Imports
from django.shortcuts import render, redirect
from .form import UploadFileForm
from .models import IPAddressModel, ResultModel
from .handlers import CrossTabHandler, GeneAndGenomeHandler

import numpy as np

# View functions
# index - /tools/crosstab/
def index(request):
    ip_address = request.META["REMOTE_ADDR"]
    if request.method == 'POST':                                                            # Checking for post method
        filled_form = UploadFileForm(request.POST, request.FILES)                           # Getting filled form details
        if filled_form.is_valid():                                                          # Validating filled form
            CrossTabHandler(filled_form.cleaned_data["file"])                               # Sending uploaded filepath to Hnadler
            title = str(filled_form.cleaned_data["file"]).split(".")[0]                     
            # Record creation in database
            ip_record = IPAddressModel.objects.create(ip_address=ip_address, title=title)
            # SESSION Variable
            request.session['job_id'] = ip_record.job_id
            return redirect("/results/{}/overview/".format(request.session['job_id']))
    else:
        empty_form = UploadFileForm()
        return render(request, 'crosstab/index.html', {
            'form': empty_form
        })

# about - /tools/crosstab/about/
def about(request):
    return render(request, 'crosstab/about.html')


