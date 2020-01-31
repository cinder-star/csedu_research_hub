from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("get_pdf/",views.get_pdf, name="get_pdf"),
]
