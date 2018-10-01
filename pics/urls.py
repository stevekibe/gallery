from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.all_pics,name='picsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    #url(r'^picture/()',views.picture,name ='picture'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)