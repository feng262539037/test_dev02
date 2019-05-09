from django.contrib import admin
from module_app.models import Module
# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','describe','create_time','project']
    # 搜索栏
    search_fields = ['name']
    # 过滤器
    list_filter = ['project']

admin.site.register(Module,ModuleAdmin)