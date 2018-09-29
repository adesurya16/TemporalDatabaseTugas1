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
    return render(request, 'temporalaps/dev.html')