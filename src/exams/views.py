from django.shortcuts import render
from .models import Exam

# Create your views here.
def index(request):
    exams = Exam.objects.prefetch_related("results").all()
    page_title = "Exams"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/exams/index.html", context)