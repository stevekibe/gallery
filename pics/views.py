from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Picture


def welcome(request):
    return render(request, 'welcome.html')

def all_pics(request):
    pics = Picture.objects.all()

    return render(request, "all-pics/today-pics.html", {"pics": pics})

def search_results(request):
    
    if 'picture' in request.GET and request.GET["picture"]:
        category = request.GET.get("picture")
        searched_pictures = Picture.search_picture(category)
        message = f"{category}"

        return render(request, 'all-pics/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-pics/search.html',{"message":message})

def filter_by_location(request,location_id):

    pictures = Picture.filter_by_location(id=location_id)
    return render(request, 'all-pics/pic.html', {"pictures": pictures})

def filter_by_category(request,category_id):
    pictures = Picture.filter_by_category(id = category_id)
    return render(request,'all-pics/category.html',{"pictures":pictures})