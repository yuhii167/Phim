from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect,render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.views.generic import View
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

#Phim
from phim.form.Register import UserRegisterForm

class UserRegisterView(View):
    """
    View đăng kí tài khoản.
    """
    template_name = 'account/register.html'
    context_object = {
        "register_form" : UserRegisterForm()
    }

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.context_object)

    def post(self, request, *args, **kwargs):
        print('hello')
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = True
            user.save()

            current_site = get_current_site(request)
            subject = 'Đã tạo tài khoản thành công'
            print(user)
            return render(request, self.template_name, self.context_object)

        else:
            messages.error(request, "Vui lòng nhập lại thông tin")
        
            return render(request, self.template_name, self.context_object)

