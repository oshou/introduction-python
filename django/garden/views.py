from django.http import HttpResponse
from django.template.response import TemplateResponse
from random import choice

name = 'ウメ'
sub_titles = ['美味しいよ!', 'お買い得!', '産地直送', 'とれたてをお届け!']


def index(request):
    title = name + 'の野菜販売'
    sub_title = choice(sub_titles)
    return TemplateResponse(request, 'garden/index.html', {'title': title, 'sub_title': sub_title})
