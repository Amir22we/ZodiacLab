from django.urls import path, include
from zodiac_finder import views

app_name = 'zodiac_finder'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_site/', views.about_site, name='about_site'),
    path('predictions_for_today/', views.predictions_for_today, name='predictions_for_today'),
    path('zodiacs/', include('zodiac_finder.zodiacs_urls')),
]

