from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("upload_file/", views.experiment, name="upload_file"),
]

if settings.DEBUG:
    urlpatterns += static(settings.PDF_URL, document_root=settings.PDF_ROOT)