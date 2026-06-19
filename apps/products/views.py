from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer