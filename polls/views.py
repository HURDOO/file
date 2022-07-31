from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')
