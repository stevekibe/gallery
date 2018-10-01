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
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

def picture(request,picture_id):
    try:
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pics/pic.html", {"picture":picture})