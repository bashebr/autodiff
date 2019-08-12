from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.template import loader

from .forms import GetVersionForm

def get_version(request):
    version_1 = ''
    version_2 = ''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetVersionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return display(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetVersionForm()

    return render(request, 'diffapp/diffapp.html', {'form': form})


def display(request):
    # process version entered by user
    version_1 = request.POST['version_1']
    version_2 = request.POST['version_2']
    return render(request, 'diffapp/display.html', {'version1': version_1, 'version2': version_2})

