# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Главная страница новостей")

def about(request):
    return HttpResponse("О нашем новостном издании")

# def index(request):
#     html = """
#     <!DOCTYPE html>
#     <html lang="ru">
#     <head>
#         <meta charset="UTF-8">
#         <title>Новостной портал</title>
#     </head>
#     <body>
#         <header>
#             <h1>Новостной портал</h1>
#         </header>
#         <main>
#             <h2>Главные новости дня</h2>
#         </main>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)

def index(request):
    return render(request, "news/index.html")

# def index(request):
#     context = {
#         "headline": "лололо",
#         "title": "В городе открылся новый парк",
#         "text": (
#             "В центральной части города открылся новый парк "
#             "с прогулочными дорожками и детской площадкой."
#         ),
#         "author": "Редакция",
#     }
#     return render(request, "news/index.html", context)

# context = {
#     "article_1": "Первая новость",
#     "article_2": "Вторая новость",
#     "article_3": "Третья новость",
# }

def index(request):
    context = {
        "title": "Главные новости дня",
        "articles": [
            "В городе открылся новый парк",
            "Учёные представили новую технологию",
            "В университете начался учебный год",
        ],
    }
    return render(request, "news/index.html", context)

def category(request):
    context = {
        "title": "Технологии",
        "articles": [
            "Представлена новая модель смартфона",
            "Компания выпустила обновление программного обеспечения",
            "Учёные разработали новый процессор",
        ],
    }
    return render(request, "news/category.html", context)


def about(request):
    context = {
        "title": "Информация о нас",
        "articles": [
            "Публикуем самые свежие новости",
            "Нашей компании уже более 15 лет",
        ],
    }
    return render(request, "news/about.html", context)


def contact(request):
    context = {
        "title": "Контактные данные",
        "articles": [
            "номер телефона",
            "имеил",
        ],
    }
    return render(request, "news/contact.html", context)