from rest_framework import generics

from phim.models.category_model import Category
from ..serializers.category_serializers import CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer