from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. Your at the polls index.")
# Create your views here.
