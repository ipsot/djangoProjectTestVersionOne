from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.template.response import TemplateResponse

from djangoProjectTest.testApp.forms import UserForm
from djangoProjectTest.testApp.models import Person


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


def base_view(request):
    return render(request, "testApp/page.html")


def form_page(request):
    userform = UserForm()
    data = {"form": userform}
    return render(request, "testApp/formpage.html", context=data)


def check_form_page(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse(f"<h2>Hello, {name} you {age}</h2>")


def persons(request):
    people = Person.objects.all()
    return render(request, "testApp/persons.html", {"people": people})
