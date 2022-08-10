import random
import uuid
import os
from urllib import parse

from django.shortcuts import render, redirect
from django.views import generic
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

from . import models


class IndexView(generic.TemplateView):
    template_name = 'index.html'


def upload(request):
    code = genCode()
    if request.method == "POST":
        file = request.FILES["file"]
        temporary = request.POST.getlist('temporary')

        uploadfile = models.Upload(
            code=code,
            index=genIndex(),
            temporary=len(temporary),
            file=file
        )
        uploadfile.save()

        return redirect("/code?code=" + str(code))

    return render(request, "upload.html")


def download(request):
    if request.method == "POST":
        return getFileResponse(request.POST['code'])

    return render(request, "download.html")


def getFileResponse(code):
    thing = models.Upload.objects.filter(code=int(code))[0]
    file_path = thing.file.path
    file_name = thing.file.name
    fs = FileSystemStorage(file_path)

    if thing.temporary:
        thing.delete()

    response = FileResponse(fs.open(file_path, 'rb'), content_type='multipart/form-data;')
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'%s' % parse.quote(file_name)
    return response


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


def code_page(request):
    code = request.GET['code']

    return render(request, "code_page.html", context={
        "code": code,
        "qr_url": "https://chart.googleapis.com/chart?cht=qr&chs=400x400&chl=https://file.gq/download?code=" + code
    })
