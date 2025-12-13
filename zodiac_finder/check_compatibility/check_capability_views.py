from openai import OpenAI
from zodiac.settings import OPENAI_API_KEY
client = OpenAI(
    api_key = OPENAI_API_KEY,
)

def translate_zodiac_signs_1(sign1: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты переводчик с английского на русский. "
                    "Переводи названия знака зодиака строго одним словом. "
                    "Ответ в формате: слово. Без лишнего текста."
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}",
            },
        ],
        temperature=0.1,
        max_tokens=20,
    )

    return completion.choices[0].message.content.strip()

def translate_zodiac_signs_2(sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты переводчик с английского на русский. "
                    "Переводи названия знака зодиака строго одним словом. "
                    "Ответ в формате: слово. Без лишнего текста."
                ),
            },
            {
                "role": "user",
                "content": f"{sign2}",
            },
        ],
        temperature=0.1,
        max_tokens=20,
    )

    return completion.choices[0].message.content.strip()

def percentage(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты профессиональный астролог. "
                    "Твоя задача — определить процент совместимости двух знаков зодиака. "
                    "Ответ строго одним токеном: N%. Где N — целое число от 0 до 100. "
                    "Запрещено добавлять любой другой текст, слова, символы или переносы строк."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}",
            },
        ],
        temperature=0.1,
        max_tokens=20,
    )

    return completion.choices[0].message.content.strip()

def short_summary(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты профессиональный астролог. "
                    "Твоя задача — кратко описать совместимость двух знаков зодиака. "
                    "Текст должен быть лаконичным, информативным и состоять из 2–3 предложений. "
                    "Без списков, без эмодзи, без приветствий и лишнего текста."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}",
            },
        ],
        temperature=0.8,
        max_tokens=150,
    )

    return completion.choices[0].message.content.strip()

def love_relationships(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты проффесиональный астролог."
                    "Твоя задача — оценить любовную совместимость двух знаков зодиака."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
        temperature=0.8,
        max_tokens=200,
    )
    
    return completion.choices[0].message.content.strip()

def friendly_relationships(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content":(
                    "Ты проффесиональный астролог."
                    "Твоя задача — оценить дружескую совместимость двух знаков зодиака."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
        temperature=0.8,
        max_tokens=200, 
    )

    return completion.choices[0].message.content.strip()

def work_and_study(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты проффесиональный астролог."
                    "Твоя задача — оценить совместимость двух знаков зодиака в работе и учебе."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
        temperature=0.8,
        max_tokens=200,
    )  

    return completion.choices[0].message.content.strip()

def energy_of_union(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты проффесиональный астролог."
                    "Твоя задача — оценить и узнать энергетику союза двух знака зодиака."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
        temperature=0.8,
        max_tokens=200,
    )

    return completion.choices[0].message.content.strip()

def pros_of_union(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты проффесиональный астролог."
                    "Твоя задача — оценить все плюсы союза двух знака зодиака."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
        temperature=0.8,
        max_tokens=200,
    )

    return completion.choices[0].message.content.strip()

def cons_of_union(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты проффесиональный астролог."
                    "Твоя задача — оценить все минусы союза двух знака зодиака."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
    )

    return completion.choices[0].message.content.strip()

def advice(sign1: str, sign2: str) -> str:
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты проффесиональный астролог."
                    "Твоя задача — дать советы двум знакам зодиака для улучшения их союза."
                    "Ответ дай кратким связным текстом из 2–3 предложений."
                    "Без списков, без эмодзи, без приветствий и лишних пояснений."
                    "Пиши только на русском языке, в том числе и знаки зодиака"
                ),
            },
            {
                "role": "user",
                "content": f"{sign1}, {sign2}"
            },
        ],
    )

    return completion.choices[0].message.content.strip()

