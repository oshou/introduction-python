from django.http import HttpResponse

name = 'ウメ'
sub_titles = ['美味しいよ!', 'お買い得!', '産地直送!', 'とれたてをお届け!']


def index(request):
    return HttpResponse('<h1>野菜販売</h1>')
