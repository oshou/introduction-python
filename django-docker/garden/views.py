from random import choice
from django.shortcuts import render
from django.template.response import TemplateResponse

from garden.models import Vegetable


# Create your views here.
name = 'ウメ'
sub_titles = ['美味しいよ!', 'お買い得!', '産地直送!', 'とれたてをお届け!']


def index(request):
    """メイン画面"""
    # タイトルを作成
    title = name+'の野菜販売'

    # サブタイトルを決定
    sub_title = choice(sub_titles)

    # 野菜一覧
    vegetables = Vegetable.objects.all()

    return TemplateResponse(request, 'garden/index.html',
                            {
                                'title': title,
                                'sub_title': sub_title,
                                'vegetables': vegetables
                            })
