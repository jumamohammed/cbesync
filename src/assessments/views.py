from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    page_title = "Assessments"
    if request.user.is_authenticated:
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/assessments/index.html", context)