from django.shortcuts import render

def about_me(request):
    return render(request, 'zodiac_finder/about_me.html')
