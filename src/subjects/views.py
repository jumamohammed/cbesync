from django.shortcuts import render
from .models import Subject

# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    page_title = "Accounts"
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/subjects/index.html", context)