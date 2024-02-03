from django.shortcuts import render
posts = [
	{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '12 мая, 2022'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '13 мая, 2022'
	}
]
def index(request):
    return render(request, "index.html")

def news(request):
    context = {
    	'posts': posts
	}
    return render(request, "news.html", context)

def contact(request):
    return render(request, "contact.html")