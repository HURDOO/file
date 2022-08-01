import random
import uuid
import os

from django.shortcuts import render
from django.views import generic
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

from . import models


class IndexView(generic.TemplateView):
    template_name = 'index.html'


def upload(request):
    if request.method == "POST":
        file = request.FILES["file"]

        uploadfile = models.Upload(
            code=genCode(),
            index=genIndex(),
            file=file
        )
        uploadfile.save()

    files = models.Upload.objects.all()

    return render(request, "upload.html", context={
        "files": files
    })


def download(request):
    if request.method == "POST":
        code = request.POST['code']

        thing = models.Upload.objects.filter(code=int(code))[0]
        file_path = thing.file.path
        fs = FileSystemStorage(file_path)

        response = FileResponse(fs.open(file_path, 'rb'), content_type='multipart/form-data;')
        response['Content-Disposition'] = f'attachment; filename={thing.file.name}'

        return response
    return render(request, "download.html")


def genCode():
    code = random.randrange(0, 1000000)
    while models.Upload.objects.filter(code=code).exists():
        code = (code + 1) % 1000000
    return code


def genIndex():
    index = uuid.uuid4()
    while models.Upload.objects.filter(index=index).exists():
        index = uuid.uuid4()
    return index
