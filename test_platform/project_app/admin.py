from django.contrib import admin
from project_app.models import Project


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time']
    # 搜索栏
    search_fields = ['name']
    # 过滤器
    list_filter = ['status']


admin.site.register(Project, ProjectAdmin)
