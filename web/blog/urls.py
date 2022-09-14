from django.urls import path
from . import views

app_name = "blog"   


urlpatterns = [
    path('', views.blog, name="blogs"),
    
    path('home/', views.HomePageView.as_view(), name="home"), # Notice the URL has been named
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('cloud/', views.CloudView.as_view(), name='cloud'),
]

