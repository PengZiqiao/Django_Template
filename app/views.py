from django.shortcuts import render


def index(request):
    title = "首页"
    header = "Django模板<small>测试版</small>"
    return render(request, "base.html", locals())
