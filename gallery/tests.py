from django.test import TestCase

# Create your tests here.
from .models import Image, Category, Location


class TestImage(TestCase):
    def setUp(self):
        self.loc = Location(location='Nakuru')
        self.loc.save_location()
        self.cat= Category(category='memes')
        self.cat.save_category()
        self.img =  Image(name ="meme",description= "a favourite meme",location = self.loc)

       
    def test_instance(self):
        self.img.save_image()
        self.assertTrue(isinstance(self.img, Image))

    def test_save_image(self):
        self.img.save_image()
        imgs = Image.objects.all()
        self.assertTrue(len(imgs) > 0)

    def test_delete_image(self):
        self.img.save_image()
        self.img.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.img.save_image()
        self.img.update_image('HI')
        img =Image.objects.filter(name='HI')
        self.assertTrue(len(img) > 0)

    def test_get_image_by_id(self):
        self.img.save_image()
        imgs =Image.get_image_by_id(self.img.id)
        self.assertEqual(imgs.id, self.img.id)

    def test_search_image(self):
        self.img.save_image()
        self.img.categories.add(self.cat)
        self.img.save_image()
        imgs = Image.search_image(self.cat.category)
        self.assertTrue(len(imgs) == 1)

    def test_filter_by_location(self):
        self.img.save_image()
        imgs = Image.filter_by_location(self.loc.location)
        self.assertTrue(len(imgs) == 1)

    def test_pictures(self):
        self.img.save_image()
        imgs = Image.pictures()
        self.assertTrue(len(imgs) > 0)
    def test_location_pictures(self):
        self.img.save_image()
        imgs = Image.location_pictures()
        self.assertTrue(len(imgs) > 0)



class TestLocation(TestCase):
    def setUp(self):
        self.loc = Location(location='Nakuru')

    def test_instance(self):
        self.assertTrue(isinstance(self.loc, Location))

    def test_save_location(self):
        self.loc.save_location()
        locs = Location.objects.all()
        self.assertTrue(len(locs) > 0)

    def test_update_location(self):
        self.loc.update_location("New England")
        locs = Location.objects.first()
        self.assertTrue(locs.location == "New England")

    def test_delete_location(self):
        self.loc.delete_location()
        locs = Location.objects.all()
        self.assertTrue(len(locs) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat = Category(category='nature')
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_category(self):
        self.cat.save_category()
        cats = Category.objects.all()
        self.assertTrue(len(cats) > 0)

    def test_delete_category(self):
        self.cat.delete_category()
        cats = Category.objects.all()
        self.assertTrue(len(cats) == 0)
    def test_update_category(self):
        self.cat.update_category("Fishing")
        cats = Category.objects.first()
        self.assertTrue(cats.category == "Fishing")