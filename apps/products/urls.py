from django.urls import path

from apps.products.views import CategoryList
from apps.products.views import CategoryDetail
from apps.products.views import ProductDetail
from apps.products.views import ProductList

app_name = "products"

urlpatterns = [
    path("category/", CategoryList.as_view(), name="category"),
    path("category/<str:pk>", CategoryDetail.as_view(), name="categories"),
    path("product/", ProductList.as_view(), name="product"),
    path("product/<str:pk>", ProductDetail.as_view(), name="products")
]