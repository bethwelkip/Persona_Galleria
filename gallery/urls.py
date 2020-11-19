from django.conf.urls import url
from . import views
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
url('^$', views.index, name = 'index'),
url('^location', views.location, name = 'location'),
url(r'^search/', views.search_results, name='search_results'),
url(r'^photo/(\d+)',views.photo,name ='photo'), 
url(r'^mode$',views.modal,name ='modal')

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)