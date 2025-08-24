from django.shortcuts import render

# Create your views here.
def index(request):
    page_title = "Accounts"
    context = {
        'page_title': page_title
    }
    return render(request, "sync_apps/accounts/index.html", context)