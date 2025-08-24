from django.shortcuts import render
from .models import Subject

# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    page_title = "Accounts"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/subjects/index.html", context)