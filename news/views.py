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

def index(request):
    context = {
        "headline": "лололо",
        "title": "В городе открылся новый парк",
        "text": (
            "В центральной части города открылся новый парк "
            "с прогулочными дорожками и детской площадкой."
        ),
        "author": "Редакция",
    }
    return render(request, "news/index.html", context)