from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
)

from apps.products.models import Category, Image, Product
from apps.products.serializers import (
    CategorySerializer,
    ImageSerializer,
    ProductSerializer,
)
from helpers.model_wrapper import RetrieveUpdateDestroyAPIViewWrapper
from helpers.renderers import DefaultRenderer


class CategoryList(ListCreateAPIView):
    """
    View to list and create a category
    """

    name = "category"
    pluralized_name = "categories"
    permission_classes = (AllowAny,)  # TODO
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = (DefaultRenderer,)

    def create(self, request, *args, **kwargs):
        self.operation = "create category"
        return super(ListCreateAPIView, self).create(request, *args, **kwargs)


class CategoryDetail(RetrieveUpdateDestroyAPIViewWrapper):
    """Class for viewing, updating and deleting a category"""

    name = "category"
    pluralized_name = "categories"
    permission_classes = (AllowAny,)  # TODO
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = (DefaultRenderer,)

    def update(self, request, *args, **kwargs):
        # overide the update method
        self.operation = "Update category"
        return super(RetrieveUpdateDestroyAPIViewWrapper, self).update(
            request, *args, **kwargs
        )


class ProductList(ListCreateAPIView):
    """
    view class to list and create a product
    """

    name = "product"
    pluralized_name = "products"
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    renderer_classes = (DefaultRenderer,)
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser,)

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
    renderer_classes = (DefaultRenderer,)
    permission_classes = (IsAuthenticatedOrReadOnly,)  # TODO
    queryset = Product.objects.all()


class ImageList(ListCreateAPIView):
    """
    View to list images
    """

    name = "image"
    pluralized_name = "images"
    permission_classes = (AllowAny,)
    queryset = Image.objects.order_by("created_at")[:5]
    serializer_class = ImageSerializer
    renderer_classes = (DefaultRenderer,)
