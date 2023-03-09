from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import View

#User
from phim.form.Login import UserLoginForm

class UserLoginView(View):
    template_name = 'account/login.html'
    context_object = {"login_form": UserLoginForm}

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,self.context_object)

    def post(self, request, *args, **kwargs):
        login_form = UserLoginForm(data=request.POST)
        print( login_form)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request,user)
                messages.success(request, f"Đăng nhập thành công!")
                return redirect('phim:home')
            else:
                messages.error(request,"Thông tin đăng nhập không hợp lệ, vui lòng kiểm tra lại!" )
                return render(request, self.template_name,self.context_object)
            
        else:
            messages.error(request, f"Tên người dùng và mật khẩu không hợp lệ")
            return render(request,self.template_name,self.context_object)
