from django.urls import path
from .views import (IndexView, ProductDetailView, ProductListView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/", ProductListView.as_view(), name="product_list"),
]
