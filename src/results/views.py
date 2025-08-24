from django.shortcuts import render
from .models import Result

# Create your views here.
def index(request):
    results = Result.objects.all()
    context = {
        'results':results
    }
    return render(request, "results/index.html", context)