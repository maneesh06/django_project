
from django.urls import path,include
from myapp import views

urlpatterns = [
    
    path('',views.index,name="home"),
    path('prashant',views.prashant,name="prashant_page"),
    path('about_us',views.about_us,name="about_us"),
    path('contact_us',views.contact_us,name="contact_us"),
    path('user',views.user_list),
    path('user/<int:pk>',views.user_detail),
    path('live_streaming',views.live_streaming,name="live_streaming"),
    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
] 