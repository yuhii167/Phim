from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView
)

class CategoriesListView(ListView):
    model = Category
    paginate_by = 12
    context_object_name = 'categories'
    template_name = 'phim/category/categories_list.html'

    def get_queryset(self):
        return Category.objects.order_by('-date_created')
    
class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name", "image"]
    template_name = 'phim/category_form.html'

    def form_valid(self, form):
        form.instance.save()
        messages.success(self.request, f"'{form.instance.name}' "
                                       f"gửi thành công. Bạn sẽ được "
                                       f"thông báo khi nó được chấp thuận."
                                       f"Cảm ơn !!!")
        return redirect('/')

