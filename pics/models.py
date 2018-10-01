from django.db import models
import datetime as dt

class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()




class Picture(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = model.ForeignKey(Location)
    category = model.ForeignKey(category)
    picture_image = models.ImageField(upload_to = 'pictures/')

    @classmethod
    def todays_pics(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics

    @classmethod
    def days_pics(cls,date):
        pics = cls.objects.filter(pub_date__date)
        return pics

    @classmethod
    def search_picture(cls,category):
        pics = cls.objects.filter(category__name__icontains=category)
        return pics


    @classmethod
    def all_pics(cls):
        pics = cls.objects.all()
        return pics

    @classmethod
    def filter_by_category(cls, id):
        pics = cls.objects.filter(category_id=id)
        return pics

    @classmethod
    def filter_by_location(cls,id):
        pics = cls.objects.filter(location_id=id)
        return pics


