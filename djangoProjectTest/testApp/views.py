from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request, pname):
    output = "say hello to, {0}".format(pname)
    return HttpResponse(output)


def index2(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = int(a) + int(b)
    output = "{0} + {1} = {2}".format(a, b, c)
    return HttpResponseServerError(output)


def index_view(request):
    countries = ["English", "German", "Spanish"]

    data = {
        "name": "Tom",
        "age": 18,
        "countries": countries
    }
    return render(request, "testApp/index.html", context=data)
