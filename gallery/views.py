from django.shortcuts import render, Http404, redirect
from .models import Image, Category
from .filldb import initialize
from django.contrib import messages
import clipboard
import pyperclip
# Create your views here.
def modal(request):
    # messages = None
    if 'copy' in request.GET and request.GET["copy"]:
        url = request.GET.get('copy')
        pyperclip.copy(url)
        # message = "Image link has been copied to clipboard"
        messages.info(request,"Image link has been copied to clipboard")
        return redirect('index')
    return render(request, 'index.html', {"messages": message})

def photo(request, photo_id):
    try:
        photo = Image.objects.get(id = photo_id)
        category = photo.categories.all()
    except:
        raise Http404()
    return render(request, 'category.html', {"photo": photo, "categories": category})

def index(request):
    # if not Image.pictures():
    #     initialize()
    # initialize()
    context = {}
    img = Category.objects.filter(category="nature").first()
    # print(img.category)
    #displays all images
    pics = Image.objects.all() #pictures()
    return render(request, 'index.html', {"pics": pics})

def location(request):
    #display based on location
    pics = Image.location_pictures()
    return render(request, 'location.html', {"pics": pics})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term \n"
        return render(request, 'search.html',{"message":message})
