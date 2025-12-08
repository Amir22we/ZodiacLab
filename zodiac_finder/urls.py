from django.urls import path
from zodiac_finder import views

app_name = 'zodiac_finder'

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('about_site/', views.about_site, name='about_site') 
]

