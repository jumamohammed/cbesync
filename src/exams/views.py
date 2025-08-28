from django.shortcuts import render
from .models import Exam

# Create your views here.
def index(request):
    page_title = "Exams"
    if request.user.is_authenticated:
        exams = Exam.objects.prefetch_related("results").all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/exams/index.html", context)