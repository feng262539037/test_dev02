__author__ = 'fengxu'
__data__ = '2019/5/6 20:49'

from django.urls import path
from testcase_app import views

urlpatterns = [
    # 用例管理
    path('', views.testcase_manage),
    # 点击发送时，调用的接口
    path('debug',views.testcase_debug),
    # 点击断言时，调用的接口
    path('assert',views.testcase_assert),

]