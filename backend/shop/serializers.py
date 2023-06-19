from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product , Category , Cart

class Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','name']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    parent = Category(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'