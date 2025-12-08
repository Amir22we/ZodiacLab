from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("aries/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/aries.html"), name="aries_page"),
    path("taurus/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/taurus.html"), name="taurus_page"),
    path("gemini/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/gemini.html"), name="gemini_page"),
    path("cancer/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/cancer.html"), name="cancer_page"),
    path("leo/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/leo.html"), name="leo_page"),
    path("virgo/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/virgo.html"), name="virgo_page"),
    path("libra/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/libra.html"), name="libra_page"),
    path("scorpio/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/scorpio.html"), name="scorpio_page"),
    path("sagittarius/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/sagittarius.html"), name="sagittarius_page"),
    path("capricorn/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/capricorn.html"), name="capricorn_page"),
    path("aquarius/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/aquarius.html"), name="aquarius_page"),
    path("pisces/", TemplateView.as_view(template_name="zodiac_finder/zodiacs/pisces.html"), name="pisces_page"),
]
