from django.shortcuts import render
from apps.products.models import Category
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.serializers import CategorySerializer
from rest_framework.generics import ListCreateAPIView
from helpers.model_wrapper import RetrieveUpdateDestroyAPIViewWrapper
from helpers.renderers import DefaultRenderer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser


class CategoryList(ListCreateAPIView):
    """
    View to list and create a category
    """
    name = "category"
    pluralized_name = "categories"
    permission_classes = (AllowAny, ) #TODO
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = (DefaultRenderer, )
    parser_classes = (FileUploadParser,MultiPartParser)

    def create(self, request, *args, **kwargs):
        self.operation = "create category"
        return super(ListCreateAPIView, self).create(request, *args, **kwargs)

class CategoryDetail(RetrieveUpdateDestroyAPIViewWrapper):
    """Class for viewing, updating and deleting a category"""
    name = "category"
    pluralized_name = "categories"
    permission_classes = (AllowAny, ) #TODO
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = (DefaultRenderer, )

    def update(self, request, *args, **kwargs):
        # overide the update method
        self.operation = "Update category"
        return super(RetrieveUpdateDestroyAPIViewWrapper, self).update(request, *args, **kwargs)


class ProductList(ListCreateAPIView):
    """
    view class to list and create a product
    """
    name = "product"
    pluralized_name = "products"
    permission_classes = (AllowAny,) #TODO
    serializer_class = ProductSerializer
    renderer_classes = (DefaultRenderer, )
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        self.operation = "create product"
        return super(ListCreateAPIView, self).create(request, *args, **kwargs)


class ProductDetail(RetrieveUpdateDestroyAPIViewWrapper):
    """
    view class to retrieve, update and delete a product
    """
    name = "product"
    pluralized_name = "products"
    serializer_class = ProductSerializer
    renderer_classes = (DefaultRenderer, )
    permission_classes = (AllowAny, ) #TODO
    queryset = Product.objects.all()


