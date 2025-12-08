from django.shortcuts import render

def about_me(request):
    return render(request, 'zodiac_finder/about_me.html')

def about_site(request):
    return render(request, 'zodiac_finder/about_site.html')