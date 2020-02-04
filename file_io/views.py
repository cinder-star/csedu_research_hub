import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from csedu_research_hub.settings import BASE_DIR
from .forms import UploadFileForm
from .utils import hash, unzip_file, make_pdf
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        hashed_name = hash(myfile.name)+".zip"
        filename = fs.save(hashed_name, myfile)
        intermediate_path = unzip_file(filename)
        pdf_file = make_pdf(intermediate_path)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': pdf_file
        })
    return render(request, 'upload.html')

def experiment(request):
    form = UploadFileForm(request.POST or None)
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        hashed_name = hash(myfile.name)+".zip"
        filename = fs.save(hashed_name, myfile)
        intermediate_path = unzip_file(filename)
        pdf_file = make_pdf(intermediate_path)
        uploaded_file_url = fs.url(filename)
        return render(request, "crispy_form.html", {"form": form, "form_title": "upload", "uploaded_file_url": pdf_file})
        # return render(request, 'upload.html', {
        #     'uploaded_file_url': pdf_file
        # })
    return render(request, "crispy_form.html", {"form": form, "form_title": "upload"})