from django.db import models
import datetime as dt

class Editor(models.Models):
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

class Pics(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    pics_image = models.ImageField(upload_to = 'pics/')

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
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics

class tags(models.Model):
     name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

