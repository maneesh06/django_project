
from django.urls import path,include
from myapp import views
urlpatterns = [
    
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
]