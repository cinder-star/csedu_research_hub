import os

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import (
    HttpResponseRedirect,
    Http404,
    HttpResponse,
    FileResponse
)
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.core.exceptions import DisallowedRedirect
from django.db import transaction

from .forms import UsersLoginForm, UsersRegisterForm
from csedu_research_hub.settings import BASE_DIR

# Create your views here.

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/upload_file/")
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect("/upload_file/")
    return render(
        request,
        "crispy_form.html",
        {"form": form, "form_title": "Login", "bg_image": "login.svg"},
    )

def get_pdf(request):
    filepath = os.path.join(BASE_DIR,"pdfs","ex3.pdf")
    return FileResponse(open(filepath,"rb"),content_type="application/pdf")

@never_cache
@transaction.atomic
def register(request):
    if request.user.is_authenticated:
        return redirect("/upload_file/")
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("/upload_file/")
    return render(
        request,
        "crispy_form.html",
        {"form": form, "form_title": "Register", "bg_image": "register.svg"},
    )

@never_cache
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")