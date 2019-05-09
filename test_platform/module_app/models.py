__author__ = 'fengxu'
__data__ = '2019/4/28 11:35'
from django.db import models
from project_app.models import Project

# 模块表
class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=60, null=False)
    describe = models.TextField('描述', default='')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name