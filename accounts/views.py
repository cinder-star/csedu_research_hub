import os

from django.shortcuts import render
from django.http import HttpResponse, Http404, FileResponse

from csedu_research_hub.firebase import firebase
from csedu_research_hub.settings import BASE_DIR

# Create your views here.

def login(request):
    email = request.GET["email"]
    password = request.GET["password"]
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return HttpResponse("success!")
    except Exception as e:
        raise Http404(e)
    return HttpResponse("ambiguous")

def get_pdf(request):
    filepath = os.path.join(BASE_DIR,"pdfs","ex3.pdf")
    return FileResponse(open(filepath,"rb"),content_type="application/pdf")