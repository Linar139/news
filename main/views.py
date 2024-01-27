from django.shortcuts import render
  
def index(request):
    return render(request, "index.html")

def news(request):
    return 
def contact(request):
    return render(request, "contact.html")
