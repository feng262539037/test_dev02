from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

# 登陆首页
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == '' or password == '':
            return render(request, 'index.html', {'error': '用户名或密码为空'})
        # 先引包
        # 通过django后台管理，验证用户名和密码
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, 'index.html', {'error': '用户名或密码错误'})
        else:
            # 1.记录用户，已经登陆的状态
            auth.login(request, user)
            # 先引包
            return HttpResponseRedirect('/project/')

# 处理用户的退出
@login_required
def logout(request):
    """
    处理用户的退出
    :param request:
    :return:
    """
    # 退出登陆，并且清除sessionid
    auth.logout(request)
    return HttpResponseRedirect('/index/')
