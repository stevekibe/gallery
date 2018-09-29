from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Pics

def welcome(request):
    return render(request, 'welcome.html')
def news_of_day(request):
    date = dt.date.today()

    #Function to convert date object to find exact day
    day = convert_dates(date)
    pics = Article.todays_news()
    return render(request, 'all-pics/today-pics.html', {"date":date, "pics":pics})

def convert_dates(dates):
    #function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',"Sunday"]

    #Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_pics(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        #raise 404 error when value error is thrown
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_day)


    pics = Article.days_news(date)
    return render(request, 'all-pics/past_pics.html', {"date": date, "pics":pics})

def new_today(request):
    date = dt.date.today()
    pics = Articles.todays_news()
    return render(request, 'all-pics/today-pics.html',{"date": date,"pics":pics})

def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pics/article.html", {"article":article})