'''
根据数据库字段自动生成页面表单的处理模块
'''
from django import forms
from .models import *


# 登录表单
class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uname', 'pwd']
        labels = {
            'uname': '用户名称',
            'pwd': '用户密码'
        }
        widgets = {
            'uname': forms.TextInput(
                attrs={
                    'placeholder': '输入您的用户名!',
                    'class': 'form-input'
                }
            ),
            'pwd': forms.PasswordInput(
                attrs={
                    'placeholder': '输入您的6-12位密码',
                    'class': 'form-input'
                }
            )
        }


# 注册表单
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uname', 'pwd', 'email', 'phone']
        labels = {
            'uname': '用户名称',
            'pwd': '用户密码',
            'email': '用户邮箱',
            'phone': '用户手机',
        }
        widgets = {
            'uname': forms.TextInput(
                attrs={
                    'placeholder': '输入您的用户名!',
                    'class': 'form-input'
                }
            ),
            'pwd': forms.PasswordInput(
                attrs={
                    'placeholder': '输入您的6-12位密码',
                    'class': 'form-input'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': '输入您的邮箱',
                    'class': 'form-input'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': '输入您的手机号',
                    'class': 'form-input'
                }
            ),
        }
