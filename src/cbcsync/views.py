from django.shortcuts import render

# Create your views here.
def index(request):
    page_title = "Home"
    context = {
        'page_title': page_title
    }
    return render(request, "index.html", context)