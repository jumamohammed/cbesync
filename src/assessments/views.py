from django.shortcuts import render

# Create your views here.
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