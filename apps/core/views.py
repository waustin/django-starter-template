from django.shortcuts import render

# A stubbed out home page to test things are working
def home(request):
    return render(request, "home.html")