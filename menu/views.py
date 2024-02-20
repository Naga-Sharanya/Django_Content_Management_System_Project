# from rest_framework import generics, permissions
# from rest_framework.exceptions import PermissionDenied
# from .models import Menu
# from .serializers import MenuSerializer

# class IsAdminOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow admin users to modify menus.
#     """

#     def has_permission(self, request, view):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD, or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Only admin users are allowed to modify (POST, PUT, DELETE) menus
#         return request.user.is_staff

# class MenuListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all().order_by('id')
#     serializer_class = MenuSerializer
#     permission_classes = [IsAdminOrReadOnly]

#     def perform_create(self, serializer):
#         if not self.request.user.is_staff:
#             raise PermissionDenied("Only admin users can create menus.")
#         serializer.save()

# class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = [IsAdminOrReadOnly]

#     def perform_update(self, serializer):
#         if not self.request.user.is_staff:
#             raise PermissionDenied("Only admin users can update menus.")
#         serializer.save()

#     def perform_destroy(self, instance):
#         if not self.request.user.is_staff:
#             raise PermissionDenied("Only admin users can delete menus.")
#         instance.delete()



from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to modify menus.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only admin users are allowed to modify (POST, PUT, DELETE) menus
        return request.user.is_staff

class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admin users can create menus.")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Menu created successfully", "status": status.HTTP_201_CREATED, "data": serializer.data}, status=status.HTTP_201_CREATED)

class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]

    def put(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admin users can update menus.")
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Menu updated successfully", "status": status.HTTP_200_OK, "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admin users can delete menus.")
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Menu deleted successfully", "status": status.HTTP_204_NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
