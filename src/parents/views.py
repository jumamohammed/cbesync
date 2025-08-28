from django.shortcuts import render
from .models import Parent

# Create your views here.
def index(request):
    page_title = "Parents"
    if request.user.is_authenticated:
        parents = Parent.objects.prefetch_related("primay_students", "secondary_students").all()
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/parents/index.html", context)