from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import OrderViewSet

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/info/', views.ProductInfoAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
    path('users/', views.UserListView.as_view()),
]

router = DefaultRouter()
router.register('orders', OrderViewSet)
urlpatterns += router.urls
