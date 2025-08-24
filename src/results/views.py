from django.shortcuts import render
from .models import Result

# Create your views here.
def index(request):
    results = Result.objects.all()
    page_title = "Results"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/results/index.html", context)