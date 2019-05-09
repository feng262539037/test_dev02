__author__ = 'fengxu'
__data__ = '2019/5/6 19:54'

from django.urls import path
from project_app import views

urlpatterns = [
    # 项目管理
    path('', views.project_manage),
    path('add_project/', views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),
    path('delete_project/<int:pid>/', views.delete_project),

    # 接口
    path('get_project_list/', views.get_project_list),

]