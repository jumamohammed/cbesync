from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
#only register a school then the school will add each student and parent..else things will be dynamic

#def login view
def login_view(request):
    page_title = "Login"
    #context just in case you i want to pass something to the login page
    context = {'page_title':page_title}
    #logic for user login
    if request.method == "POST":
        username =request.POST.get("username") or None
        password =request.POST.get("password") or None
        #eval(print("hello"))
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
                # Redirect to a success page.
    return render(request, "sync_apps/auth/login.html", context)

#school register view
def register_view(request):
    page_title = "Register"
    context = {'page_title':page_title}
    #logic for user register
    if request.method == "POST":
        username =request.POST.get("username") or None
        email = request.POST.get("email") or None
        password =request.POST.get("password") or None
        #eval(print("hello"))
        if all([username, password, email]):
            #check if the username or the email already exists in the database
            #Django forms does this really well
            # username_exists_qs = User.objects.filter(username__iexact=username).exists()
            # email_exists_qs = User.objects.filter(email__iexact=email).exists()
            try:
                User.objects.create_user(username, email=email, password=password)
            except:
                pass
            return redirect("/")
            # Redirect to a success page.

    return render(request, "sync_apps/auth/register.html", context)
