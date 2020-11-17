from django.db import models
from cloudinary.models import  CloudinaryField
import datetime as dt
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    def update_category(self, new_category):
        self.update(category = new_category)

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    def update_location(self, new_location):
        self.update(location =new_location)

class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    categories = models.ManyToManyField(Category)
    image = CloudinaryField('image', null = True, blank = True)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    def update_image(self, new_name):
        self.update(name = new_name)
    
    @classmethod
    def get_image_by_id(cls, id):
        photo = cls.objects.get(id = id)
        return photo
        # cls.objects.
    
    @classmethod
    def search_image(cls, category):
        images = cls.objects.filter(categories__category__icontains = category)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location = location)
        return images
    @classmethod
    def pictures(cls):  
        picture = cls.objects.all()
        pics = [pic.image for pic in picture if pic.image]
        return pics
    @classmethod
    def location_pictures(cls):  
        locs = ["Princeton","Nakuru", "Wawa", "Nairobi", "Beach"]
        picture = cls.objects.all()
        pics = list()
        for loc in locs:
            pics.append([pic.image for pic in picture if pic.location.location == loc])
        return pics


    
