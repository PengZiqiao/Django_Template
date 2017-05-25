from django.shortcuts import render


def navbar(request):
    """
    返回用于生成导航栏的字典
    
    key 为在导航中显示的名称
    value 为在urls中设置路由时，name参数的值
    cuurent_link 为当前url
    
    在每个视图中加入 nav,current_link = navbar(request)以传递该字典给模板
    """
    nav = {
        '首页': 'index',
        '测试': 'test',
    }
    current_link = request.path
    return nav, current_link


def index(request):
    title = "首页"
    header = "Django试验<small>测试版</small>"
    nav, current_link = navbar(request)
    return render(request, "index.html", locals())


def test1(request):
    title = "测试1"
    header = "测试1<small>这是个测试页面</small>"
    nav, current_link = navbar(request)
    return render(request, "test1.html", locals())
