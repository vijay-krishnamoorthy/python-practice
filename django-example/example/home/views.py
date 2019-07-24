from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<center><h1>Home page</h1></center>")

def about(request):
    return HttpResponse("<center><h1>About page</h1></center>")
 