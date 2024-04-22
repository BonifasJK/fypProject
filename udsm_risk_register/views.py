from django.shortcuts import render

#Home Page
def home(request):
    return render(request, "home.html")

#Login Page
def login(request):
    return render(request, "login.html")


