from rest_framework import serializers
from .models import User, Role, Permissions
from django.contrib.auth.tokens import default_token_generator


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=120)

    class Meta:
        model = User
        fields = ["email", "password", "confirm_password"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            # mobile_number=validated_data["mobile_number"],
            password=validated_data["password"],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

        
class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ['id', 'role', 'permission']

    def validate(self, data):
        # Check if the user has the required role to grant or update permissions
        user = self.context['request'].user
        if user.is_authenticated and user.roles.filter(role='admin').exists():
            return data
        else:
            raise serializers.ValidationError("You do not have the permission to manage permissions.")

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class ForgetPasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        # You can add custom validation logic here if needed
       return data