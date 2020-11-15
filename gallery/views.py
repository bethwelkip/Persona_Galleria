from django.shortcuts import render
from .models import Image
# Create your views here.
def profile(request):
    #displays by category
    return render(request, 'category.html')

def index(request):
    #displays all images
    return render(request, 'index.html')

def location(request):
    #display based on location
    return render(request, 'location.html')

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"articles": searched_articles})
    elif 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term \n"
        return render(request, 'search.html',{"message":message})
