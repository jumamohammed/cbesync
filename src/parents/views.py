from django.shortcuts import render
from .models import Parent

# Create your views here.
def index(request):
    parents = Parent.objects.prefetch_related("primay_students", "secondary_students").all()
    page_title = "Parents"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/parents/index.html", context)