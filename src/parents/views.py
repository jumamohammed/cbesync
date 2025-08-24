from django.shortcuts import render
from .models import Parent

# Create your views here.
def index(request):
    parents = Parent.objects.prefetch_related("primay_students", "secondary_students").all()
    context = {
        'parents':parents
    }
    return render(request, "parents/index.html", context)