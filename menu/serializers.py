# menu/serializers.py
from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'slug', 'link']

# from rest_framework import serializers
# from rest_framework.exceptions import PermissionDenied
# from .models import Menu

# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = ['id', 'name', 'slug', 'link']

#     def create(self, validated_data):
#         request = self.context.get('request')
#         if request and (request.user.is_authenticated and request.user.is_staff):
#             return super().create(validated_data)
#         else:
#             raise PermissionDenied("Only authenticated admin users can create menus.")

#     def update(self, instance, validated_data):
#         request = self.context.get('request')
#         if request and (request.user.is_authenticated and request.user.is_staff):
#             return super().update(instance, validated_data)
#         else:
#             raise PermissionDenied("Only authenticated admin users can update menus.")

#     def delete(self, instance):
#         request = self.context.get('request')
#         if request and (request.user.is_authenticated and request.user.is_staff):
#             instance.delete()
#         else:
#             raise PermissionDenied("Only authenticated admin users can delete menus.")
