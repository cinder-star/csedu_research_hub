from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view, name="log_in"),
    path("get_pdf/",views.get_pdf, name="get_pdf"),
    path("register/", views.register ,name="register"),
    path("log_out/",views.logout_view, name="log_out"),
]
