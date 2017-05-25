from django.shortcuts import render


def index(request):
    title = "首页"
    name = "peng"
    return render(request, "base.html", locals())
