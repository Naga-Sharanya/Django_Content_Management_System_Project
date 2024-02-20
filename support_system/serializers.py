# serializers.py
from rest_framework import serializers
from .models import Ticket
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class TicketSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(max_length=120, read_only=True)
    solution = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Ticket
        fields = ['id', 'issue', 'description', 'created_at', 'updated_at', 'status', 'created_by', 'solution']

    # Add the permission_classes attribute to specify permissions for the serializer
    permission_classes = [IsAuthenticated]

    def get_created_by(self, obj):
        if obj and obj.created_by:
            return obj.created_by.username  # Return the username instead of just accessing it

    def create(self, validated_data):
        # Check if the user is authenticated before creating the ticket
        if self.context['request'].user.is_authenticated:
            validated_data['created_by'] = self.context['request'].user

            # # Check if a solution is provided and update the status accordingly
            # if 'solution' in validated_data and validated_data['solution']:
            #     validated_data['status'] = 'resolved'

            return Ticket.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("User must be authenticated to create a ticket.")

    def update(self, instance, validated_data):
        # Check if the user is authenticated before updating the ticket
        if self.context['request'].user.is_authenticated:
            instance.issue = validated_data.get('issue', instance.issue)
            instance.description = validated_data.get('description', instance.description)
            instance.solution = validated_data.get('solution', instance.solution)

            # Update status to "resolved" if a solution is provided
            if instance.solution:
                instance.status = 'resolved'

            instance.save()
            return instance
        else:
            raise serializers.ValidationError("User must be authenticated to update a ticket.")

    def validate(self, data):
        user = self.context['request'].user

        # Check if the user is an admin when trying to post a solution
        if user and user.is_staff and 'solution' in data:
            return data
        elif 'solution' in data:
            raise serializers.ValidationError("Only admin users can post solutions.")

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user

        # Only include the "solution" field if the user is an admin
        if user and user.is_staff:
            return data
        else:
            # Exclude the "solution" field for non-admin users
            data.pop('solution', None)
            return data






# from rest_framework import serializers
# from .models import Ticket
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from category.models import Category

# class TicketSerializer(serializers.ModelSerializer):
#     created_by = serializers.CharField(max_length=120, read_only=True)
#     solution = serializers.CharField(allow_blank=True, required=False)
#     category = serializers.CharField(max_length=120, write_only=True)

#     class Meta:
#         model = Ticket
#         fields = ['id', 'issue', 'description', 'created_at', 'updated_at', 'status', 'created_by', 'solution', 'category']

#     permission_classes = [IsAuthenticated]

#     def get_created_by(self, obj):
#         if obj and obj.created_by:
#             return obj.created_by.username

#     def validate_category(self, value):
#         # Check if the provided category exists
#         category_instance = Category.objects.filter(category=value).first()
#         if not category_instance:
#             raise serializers.ValidationError("Category mismatched.")
#         return value

#     def create(self, validated_data):
#         if self.context['request'].user.is_authenticated:
#             validated_data['created_by'] = self.context['request'].user
#             category_name = validated_data.get('category')
#             category_instance = Category.objects.filter(category=category_name).first()

#             if category_instance:
#                 validated_data['category'] = category_instance
#                 return Ticket.objects.create(**validated_data)
#             else:
#                 raise serializers.ValidationError("Category mismatched.")
#         else:
#             raise serializers.ValidationError("User must be authenticated to create a ticket.")

#     def update(self, instance, validated_data):
#         if self.context['request'].user.is_authenticated:
#             instance.issue = validated_data.get('issue', instance.issue)
#             instance.description = validated_data.get('description', instance.description)
#             instance.solution = validated_data.get('solution', instance.solution)
#             instance.status = validated_data.get('status', instance.status)

#             category_name = validated_data.get('category')
#             category_instance = Category.objects.filter(category=category_name).first()

#             if category_instance:
#                 instance.category = category_instance
#                 instance.save()
#                 return instance
#             else:
#                 raise serializers.ValidationError("Category mismatched during update.")
#         else:
#             raise serializers.ValidationError("User must be authenticated to update a ticket.")

#     def validate(self, data):
#         user = self.context['request'].user

#         # Check if the user is an admin when trying to post a solution
#         if user and user.is_staff and 'solution' in data:
#             return data
#         elif 'solution' in data:
#             raise serializers.ValidationError("Only admin users can post solutions.")

#         return data

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         user = self.context['request'].user

#         # Only include the "solution" field if the user is an admin
#         if user and user.is_staff:
#             return data
#         else:
#             # Exclude the "solution" field for non-admin users
#             data.pop('solution', None)
#             return data

