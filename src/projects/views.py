from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    page_title = "Projects"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/projects/index.html", context)