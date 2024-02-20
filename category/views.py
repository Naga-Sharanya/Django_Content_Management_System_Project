from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Content
from .serializers import CategorySerializer, ContentSerializer
from rest_framework.permissions import IsAuthenticated

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Content.objects.filter(is_deleted=False).order_by('created_at')
    serializer_class = ContentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Content created successfully.", "status": status.HTTP_201_CREATED})

class ContentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    
class ContentArchiveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        if content.created_by == request.user:
            content.archived = True
            content.save()
            return Response({"message": "Content archived successfully.", "status": status.HTTP_200_OK})
        else:
            return Response({"error": "You are not authorized to archive this content.", "status": status.HTTP_403_FORBIDDEN})

class ArchivedContentListAPIView(generics.ListAPIView):
    queryset = Content.objects.filter(archived=True)
    serializer_class = ContentSerializer
    
class ContentUnarchiveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        if content.created_by == request.user:
            content.archived = False
            content.save()
            return Response({"message": "Content unarchived successfully.", "status": status.HTTP_200_OK})
        else:
            return Response({"error": "You are not authorized to unarchive this content.", "status": status.HTTP_403_FORBIDDEN})

class ContentSoftDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        if content.created_by == request.user:
            content.is_deleted = True
            content.save()
            return Response({"message": "Content soft deleted successfully.", "status": status.HTTP_200_OK})
        else:
            return Response({"error": "You are not authorized to soft delete this content.", "status": status.HTTP_403_FORBIDDEN})

class ContentRestoreAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        if content.created_by == request.user:
            content.is_deleted = False
            content.save()
            return Response({"message": "Content restored successfully.", "status": status.HTTP_200_OK})
        else:
            return Response({"error": "You are not authorized to restore this content.", "status": status.HTTP_403_FORBIDDEN})


# from rest_framework import generics, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from .models import Category, Content
# from .serializers import CategorySerializer, ContentSerializer
# from rest_framework.permissions import IsAuthenticated

# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class ContentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Content.objects.filter(is_deleted=False).order_by('created_at')  # Order by created_at
#     serializer_class = ContentSerializer

# # class ContentListCreateAPIView(generics.ListCreateAPIView):
# #     queryset = Content.objects.filter(is_deleted=False)  # Exclude soft-deleted items
# #     serializer_class = ContentSerializer

# class ContentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Content.objects.all()
#     serializer_class = ContentSerializer
    
# class ContentArchiveAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         content = get_object_or_404(Content, pk=pk)
#         if content.created_by == request.user:  # Ensure the user is the creator of the content
#             content.archived = True
#             content.save()
#             return Response({"message": "Content archived successfully."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "You are not authorized to archive this content."}, status=status.HTTP_403_FORBIDDEN)

# class ArchivedContentListAPIView(generics.ListAPIView):
#     queryset = Content.objects.filter(archived=True)  # Query only archived content
#     serializer_class = ContentSerializer
    
    
    
# class ContentUnarchiveAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         content = get_object_or_404(Content, pk=pk)
#         if content.created_by == request.user:  # Ensure the user is the creator of the content
#             content.archived = False
#             content.save()
#             return Response({"message": "Content unarchived successfully."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "You are not authorized to unarchive this content."}, status=status.HTTP_403_FORBIDDEN)
        
        
        
# class ContentSoftDeleteAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         content = get_object_or_404(Content, pk=pk)
#         if content.created_by == request.user:  # Ensure the user is the creator of the content
#             content.is_deleted = True
#             content.save()
#             return Response({"message": "Content soft deleted successfully."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "You are not authorized to soft delete this content."}, status=status.HTTP_403_FORBIDDEN)
        
        
        
# class ContentRestoreAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, pk):
#         content = get_object_or_404(Content, pk=pk)
#         if content.created_by == request.user:  # Ensure the user is the creator of the content
#             content.is_deleted = False  # Restore the content
#             content.save()
#             return Response({"message": "Content restored successfully."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "You are not authorized to restore this content."}, status=status.HTTP_403_FORBIDDEN)



