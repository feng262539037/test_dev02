from django.db import models

# Create your models here.

# 项目表
class Project(models.Model):
    name = models.CharField('名称', max_length=60, null=False)
    describe = models.TextField('描述', default='')
    # 1 是 True
    status = models.BooleanField('状态', default=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name