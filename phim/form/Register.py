from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Form đăng kí
class UserRegisterForm(UserCreationForm):
    """
        Thông tin đăng kí
    """
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus",None)

    email = forms.EmailField(max_length=200, required=True, widget=
                             forms.EmailInput(attrs={
                                "name" : "email", "class" : "input100",
                                "placeholder" : "Email"
                             }),
                             help_text='Vui lòng nhập Email của bạn!'
                             )
    password1 = forms.CharField(widget=
                               forms.PasswordInput(attrs={
                                    "name" : "password", "class" : "input100",
                                    "placeholder" : " Mật khẩu"
                               }),
                               help_text='Nhập mật khẩu'
                               )
    password2 = forms.CharField(widget=
                               forms.PasswordInput(attrs={
                                    "name" : "password", "class" : "input100",
                                    "placeholder" : " Mật khẩu"
                               }),
                               help_text='Xác nhận lại mật khẩu'
                                )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {

            "username": forms.TextInput(attrs={
                "name": "username", "class" : "input100",
                "placeholder" : "Tên tài khoản"
            })
        }