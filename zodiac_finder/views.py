from django.shortcuts import render, redirect
from .zodiac_data import ZODIAC_DATES
from openai import OpenAI
from zodiac.settings import OPENAI_API_KEY, OPENAI_BASE_URL
from .check_compatibility import check_capability_views
client = OpenAI(
    api_key = OPENAI_API_KEY,
    base_url = OPENAI_BASE_URL
)

def predictions_for_today(request):
    if request.method == "POST":
         completion = client.chat.completions.create(
            extra_body={},
            model="openai/gpt-5.2-chat",
            messages=[
                 {
                      "role": "system",
                      "content": (
                            "Ты профессиональный астролог. "
                            "Твоя задача — писать короткие, но ёмкие и атмосферные гороскопы на русском языке, которые создают настроение и легко читаются. Каждый гороскоп должен быть эмоционально насыщенным, образным и интуитивно понятным, без перегруза деталями и сухой астрологической терминологией. Текст должен ощущаться как личное обращение к читателю, вызывать ощущение вовлечённости и внутреннего отклика."
                            "В гороскопах отражай общее энергетическое состояние периода, внутренние переживания, настроение, возможные импульсы и скрытые тенденции. Допускается мягкая философская подача, метафоры и ассоциации, но без мистического абсурда и запугивания. Делай акцент на чувствах, решениях, настроении и внимании к себе."
                            "Каждый текст должен содержать ненавязчивые подсказки или ориентиры: на что стоит обратить внимание, где лучше замедлиться, а где проявить инициативу. Избегай прямых приказов и категоричных прогнозов, формулируй мысли аккуратно и тактично. Гороскоп должен оставлять после себя ощущение ясности, спокойствия или лёгкого внутреннего импульса к действию, даже если речь идёт о сложных темах."
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

def check_compatibility(request):
    if request.method == "POST":
        first_sign = request.POST.get("sign_1")
        second_sign = request.POST.get("sign_2")

        translated_first_sign = check_capability_views.translate_zodiac_signs_1(first_sign)
        translated_second_sign = check_capability_views.translate_zodiac_signs_2(second_sign)
 
        percentage = check_capability_views.percentage(first_sign, second_sign)

        short_summary = check_capability_views.short_summary(first_sign, second_sign)

        love_relationships = check_capability_views.love_relationships(first_sign, second_sign)

        friendly_relationships = check_capability_views.friendly_relationships(first_sign, second_sign)

        work_and_study = check_capability_views.work_and_study(first_sign, second_sign)

        energy_of_union = check_capability_views.energy_of_union(first_sign, second_sign)

        pros_of_union = check_capability_views.pros_of_union(first_sign, second_sign)

        cons_of_union = check_capability_views.cons_of_union(first_sign, second_sign)

        advice = check_capability_views.advice(first_sign, second_sign) 

        context = {
            "first_sign": translated_first_sign,
            "second_sign": translated_second_sign,
            "percentage": percentage,
            "short_summary": short_summary,
            "love_relationships": love_relationships,
            "friendly_relationships": friendly_relationships,
            "work_and_study": work_and_study,
            "energy_of_union": energy_of_union,
            "pros_of_union": pros_of_union,
            "cons_of_union": cons_of_union,
            "advice": advice
        }

        return render(request, 'zodiac_finder/check_compatibility_result.html', context)
    return render(request, 'zodiac_finder/check_compatibility.html')

