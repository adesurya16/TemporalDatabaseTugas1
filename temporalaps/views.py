from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    template = "<h1> hai </h1>"
    context = Context({ "panggilan" : "hai" })
    # return HttpResponse(template.render(context))
    # return render(request, 'temporalaps/index.html')
    return render(request, 'temporalaps/templates/temporalaps/nav.html')

def showentity(request):
    return render(request, 'temporalaps/templates/temporalaps/er.html')

def showrelational(request):
    return render(request, 'temporalaps/templates/temporalaps/relational.html')

def inputquery(request):
    return render(request, 'temporalaps/templates/temporalaps/query.html')

def showabout(request):
    return render(request, 'temporalaps/templates/temporalaps/about.html')