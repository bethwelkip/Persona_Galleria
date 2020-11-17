from .models import Image, Category, Location
import random
from random import shuffle
import cloudinary, cloudinary.api,cloudinary.uploader
import os
def initialize():
    cwd = os.getcwd()
    # image = cloudinary.uploader.upload_resource(f'https://github.com/bethwelkip/Persona_Galleria/tree/master/gallery/assets/memes/0.JPG')
    #name, description, location,categories, image
    locations = ["Princeton","Nakuru", "Wawa", "Nairobi", "Beach"]
    categories = ["memes", "nature", "bethwel", "friends"]

    for location in locations:
        loc = Location(location = location)
        loc.save()
    for category in categories:
        cat = Category(category = category)
        cat.save()

    locs = [loc for loc in Location.objects.all()]
    cats = Category.objects.all()
    for i in range(5):
        img = Image(name ="meme",description= "a favourite meme",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'{cwd}/gallery/assets/memes/{i}.JPG')
        # img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/memes/{i}.JPG')
        img.save()
        img.categories.add(Category.objects.filter(category="memes").first())
        img.save()
    for i in range(9):
        img = Image(name ="walk",description= "a pic of the place I hang out mostly",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'{cwd}/gallery/assets/nature/{i}.jpg')
        # img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/nature/{i}.jpg')

        img.save()
        img.categories.add(Category.objects.filter(category="nature").first())
        img.save()
    for i in range(7):
        img = Image(name ="Me",description= "a pic of myself and my friends",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'{cwd}/gallery/assets/bethwel/{i}.jpg')
        # img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/bethwel/{i}.jpg')
        img.save()
        img.categories.add(Category.objects.filter(category="bethwel").first())
        img.categories.add(Category.objects.filter(category="friends").first())
        img.save()
    for i in range(7):
        img = Image(name ="Me",description= "a pic of myself and my friends",location = random.choice(locs))
        img.image = cloudinary.uploader.upload_resource(f'{cwd}/gallery/assets/fun/{i}.jpg')
        # img.image = cloudinary.uploader.upload_resource(f'/Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/fun/{i}.jpg')
        img.save()
        img.categories.add(Category.objects.filter(category="nature").first())
        img.categories.add(Category.objects.filter(category="bethwel").first())
        img.categories.add(Category.objects.filter(category="friends").first())
        img.save()
    pics = [img.name for img in Image.objects.all()]
    # /Users/bethwelkiplimo/Desktop/MoringaCore/PersonaGalleria/gallery/assets/