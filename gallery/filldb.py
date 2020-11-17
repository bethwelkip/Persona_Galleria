from .models import Image, Category, Location
import random
from random import shuffle
import cloudinary, cloudinary.api,cloudinary.uploader

def initialize():
    #name, description, location,categories, image
    locations = ["Princeton","Nakuru", "Wawa", "Nairobi", "Beach"]
    categories = ["memes", "nature", "bethwel", "friends"]
    # shuffle(locations)
    # shuffle(categories)
    # meme = f'/assets/memes/{locations[0]}.JPG'
    for location in locations:
        loc = Location(location = location)
        loc.save()
    for category in categories:
        cat = Category(category = category)
        cat.save()

    locs = [loc for loc in Location.objects.all()]
    cats = Category.objects.all()
    for i in range(15):
        img = Image(name ="meme",description= "a favourite meme",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/memes/{i}.JPG')
        img.save()
        img.categories.add(random.choice(cats))
        img.save()
    for i in range(6):
        img = Image(name ="walk",description= "a pic of the place I hang out mostly",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/nature/{i}.jpg')
        img.save()
        img.categories.add(random.choice(cats))
        img.save()
    for i in range(7):
        img = Image(name ="Me",description= "a pic of myself and my friends",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/bethwel/{i}.jpg')
        img.save()
        img.categories.add(random.choice(cats))
        img.categories.add(random.choice(cats))
        img.save()
    pics = [img.name for img in Image.objects.all()]
    print(pics)
    # /Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/