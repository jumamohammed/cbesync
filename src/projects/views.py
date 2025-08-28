from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    page_title = "Projects"
    if request.user.is_authenticated:
        projects = Project.objects.all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/projects/index.html", context)