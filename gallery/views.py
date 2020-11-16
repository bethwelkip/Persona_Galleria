from django.shortcuts import render
from .models import Image
from .filldb import initialize
# Create your views here.
def profile(request):
    #displays by category
    return render(request, 'category.html')

def index(request):
    if not Image.pictures():
        initialize()
    #displays all images
    pics = Image.pictures()
    print(pics[0].url)
    return render(request, 'index.html', {"pics": pics})

def location(request):
    #display based on location
    pics = Image.objects.all()
    print(pics[4].location)
    return render(request, 'location.html', {"pics": pics})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})
    elif 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term \n"
        return render(request, 'search.html',{"message":message})
