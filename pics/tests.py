from django.test import TestCase
from .models import Editor,Picture,tags
import datetime as datetime

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class PictureTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_picture= Picture(title = 'Test Picture',post = 'This is a random test Post',editor = self.james)
        self.new_picture.save()

        self.new_picture.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
    
    def test_get_pics_today(self):
        today_pics= Picture.todays_pics()
        self.assertTrue(len(today_pics)>0)

    def test_get_pics_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        pics_by_date = Picture.days_pics(date)
        self.assertTrue(len(pics_by_date) == 0)
