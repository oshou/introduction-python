from django.http.response import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>HelloWorld</h1>")
