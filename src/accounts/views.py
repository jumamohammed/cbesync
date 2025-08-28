from django.shortcuts import render

# Create your views here.
def index(request):
    page_title = "Accounts"
    if request.user.is_authenticated:
        context = {
            'page_title': page_title
        }
    else:
        context = {
            'page_title': page_title
        }
    return render(request, "sync_apps/accounts/index.html", context)