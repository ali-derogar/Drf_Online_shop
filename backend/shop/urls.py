from django.contrib import admin
from django.urls import path , include
from .views import CategoryViewSet , ProductViewSet , CartViewSet , UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('cart', CartViewSet, basename='cart')


app_name = "shop"
urlpatterns = router.urls