# coding=utf8
from django import forms

class RegisterForm(forms.Form):
     username = forms.CharField(required=True,
                                min_length=3,
                                max_length=20)
     password1 = forms.CharField(required=True,
                                 min_length=8,
                                 max_length=20)
     password2 = forms.CharField(required=True,
                                 min_length=8,
                                 max_length=20)
     email = forms.EmailField(required=True)


     def clean_password2(self):
         """
            两次密码的验证
         """
         password1 = self.cleaned_data["password1"]
         password2 = self.cleaned_data["password2"]
         if password1 != password2:
             raise forms.ValidationError(u"两次密码不一致", code="password2")
         return password2


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, required=True)
    password = forms.CharField(min_length=8, max_length=20, required=True)