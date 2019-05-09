__author__ = 'fengxu'
__data__ = '2019/5/6 20:14'

from django import forms
from module_app.models import Module


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']
