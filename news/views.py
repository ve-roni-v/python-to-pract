# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.

# def index(request):
#     return HttpResponse("Главная страница новостей")

def index(request):
    articles = Article.objects.filter(
        is_published=True
    ).order_by("-created_at")

    context = {
        "articles": articles,
    }

    return render(
        request,
        "news/index.html",
        context,
    )

def about(request):
    return HttpResponse("О нашем новостном издании")


# def index(request):
#     return render(request, "news/index.html")

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

# def index(request):
#     context = {
#         "title": "Главные новости дня",
#         "articles": [
#             "В городе открылся новый парк",
#             "Учёные представили новую технологию",
#             "В университете начался учебный год",
#         ],
#     }
#     return render(request, "news/index.html", context)

# def category(request):
#     context = {
#         "title": "Технологии",
#         "articles": [
#             "Представлена новая модель смартфона",
#             "Компания выпустила обновление программного обеспечения",
#             "Учёные разработали новый процессор",
#         ],
#     }
#     return render(request, "news/category.html", context)

def category(request, category_name=None):
    if category_name is None:
        articles = Article.objects.filter(
            is_published=True
        ).order_by("-created_at")

        category_name = "Все категории"
    else:
        articles = Article.objects.filter(
            is_published=True,
            category__iexact=category_name,
        ).order_by("-created_at")

    context = {
        "articles": articles,
        "category_name": category_name,
    }

    return render(
        request,
        "news/category.html",
        context,
    )



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


def article_detail(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id,
        is_published=True,
    )

    context = {
        "article": article,
    }

    return render(
        request,
        "news/article_detail.html",
        context,
    )