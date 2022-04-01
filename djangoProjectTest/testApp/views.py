from django.http import HttpResponse, HttpResponseServerError

def index(request, pname):
    output = "say hello to, {0}".format(pname)
    return HttpResponse(output)

def index2(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = int(a)+int(b)
    output = "{0} + {1} = {2}".format(a,b,c)
    return HttpResponseServerError(output)
