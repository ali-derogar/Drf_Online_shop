from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Product , Category , Cart
from .serializers import ProductSerializer , CartSerializer , CategorySerializer , UserSerializer
from .permissions import IsSupperUser , IsSuperUserOrStaffReadOnly , IsStaffOrReadOnly , IsAuthorOrReadOnly , IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from .pagination import LargeResultsSetPagination

    
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['price', 'status']
    search_fields = ['model', 'price']
    ordering_fields = ['price']
    pagination_class = LargeResultsSetPagination
    
    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsStaffOrReadOnly,]
        else:
            permission_classes = [IsAuthorOrReadOnly,IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]
    
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        if (self.action in ['list','create']):
            permission_classes = [IsSuperUserOrStaffReadOnly,]
        else:
            permission_classes = [IsSupperUser,]
        return [permission() for permission in permission_classes]
    
class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    ordering_fields = ['-pk']
    
    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsOwnerOrReadOnly,]
        else:
            permission_classes = [IsSupperUser,IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
    
class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if (self.action in ['list','create']):
            permission_classes = [IsSuperUserOrStaffReadOnly,]
        else:
            permission_classes = [IsSupperUser,]
        return [permission() for permission in permission_classes]