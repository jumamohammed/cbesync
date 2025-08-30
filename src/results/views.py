from django.shortcuts import render
from .models import Result
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    page_title = "Results"
    if request.user.is_authenticated:
        results = Result.objects.all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/results/index.html", context)