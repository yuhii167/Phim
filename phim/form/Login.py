from django import forms

#Form đăng nhập
class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "name" : "username", 
        "placeholder": "Tài khoản"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "name":"password",
        "placeholder":"Mật khẩu"
    }))