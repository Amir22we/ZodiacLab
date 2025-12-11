from django.shortcuts import render, redirect
from django.http import HttpResponse
from .zodiac_data import ZODIAC_DATES
from openai import OpenAI
from zodiac.settings import OPENAI_API_KEY, OPENAI_BASE_URL
client = OpenAI(
    api_key = OPENAI_API_KEY,
    base_url = OPENAI_BASE_URL
)

def predictions_for_today(request):
    if request.method == "POST":
         completion = client.chat.completions.create(
            extra_body={},
            model="openai/gpt-5.1",
            messages=[
                 {
                      "role": "system",
                      "content": (
                            "Ты профессиональный астролог. "
                            "Пишешь короткие, атмосферные гороскопы на русском языке. "
                            "Без упоминаний ИИ, нейросетей и технологий."
                      ),
                 },
                 {
                      "role": "user",
                      "content": (
                           f"Придумай прикольное предсказание на русском на сегоднешний день"
                           "3–5 предложений. Стиль: живой, мистический, современныйю. Пиши не используя сложные словосочетания и слова."
                      ),
                 },
            ],
            temperature=0.9,
            max_tokens=300,
         )

         astro_text = completion.choices[0].message.content.strip()
         return render(request, "zodiac_finder/prediction_result.html", {"astro_text": astro_text})
    return render(request, 'zodiac_finder/predictions_for_today.html')
def generate_full_zodiac_map():
            result = {}
            for sign, ((start_month, start_day), (end_month, end_day)) in ZODIAC_DATES.items():
                month_sign = start_month
                day_sign = start_day

                while True:
                    result[(month_sign, day_sign)] = sign

                    if (month_sign, day_sign) == (end_month, end_day):
                        break

                    day_sign += 1
                    if day_sign > 31:
                        day_sign = 1
                        month_sign += 1
                        if month_sign > 12:
                            month_sign = 1
            return result

FULL_ZODIAC_MAP = generate_full_zodiac_map()

def index(request):
    if request.method == "POST":
        date = request.POST.get('birth_date')
        updated_date = date[4:].replace('-', '')
        month = int(updated_date[:-2])
        day = int(updated_date[2:])
        data = (month, day)
        
        sign = FULL_ZODIAC_MAP.get(data, "unknown")
        HANDLERS = {
            "aries": "zodiac_finder:aries_page",
            "taurus": "zodiac_finder:taurus_page",
            "gemini": "zodiac_finder:gemini_page",
            "cancer": "zodiac_finder:cancer_page",
            "leo": "zodiac_finder:leo_page",
            "virgo": "zodiac_finder:virgo_page",
            "libra": "zodiac_finder:libra_page",
            "scorpio": "zodiac_finder:scorpio_page",
            "sagittarius": "zodiac_finder:sagittarius_page",
            "capricorn": "zodiac_finder:capricorn_page",
            "aquarius": "zodiac_finder:aquarius_page",
            "pisces": "zodiac_finder:pisces_page",
        }

        handler = HANDLERS.get(sign)
        if handler:
            return redirect(handler)

    return render(request, 'zodiac_finder/index.html')

def about_me(request):
    return render(request, 'zodiac_finder/about_me.html')

def about_site(request):
    return render(request, 'zodiac_finder/about_site.html')

