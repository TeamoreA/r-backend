from django.urls import path

from apps.products.views import (
    CategoryDetail,
    CategoryList,
    ImageList,
    ProductDetail,
    ProductList,
)

app_name = "products"

urlpatterns = [
    path("category/", CategoryList.as_view(), name="category"),
    path("category/<str:pk>", CategoryDetail.as_view(), name="categories"),
    path("product/", ProductList.as_view(), name="products"),
    path("image/", ImageList.as_view(), name="images"),
    path("product/<str:pk>", ProductDetail.as_view(), name="product"),
]
