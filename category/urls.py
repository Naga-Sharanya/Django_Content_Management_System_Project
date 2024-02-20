# from django.urls import path
# from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView
# from .views import ContentListCreateAPIView, ContentRetrieveUpdateDestroyAPIView

# urlpatterns = [
#     path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
#     path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
#     path('contents/', ContentListCreateAPIView.as_view(), name='content-list-create'),
#     path('contents/<int:pk>/', ContentRetrieveUpdateDestroyAPIView.as_view(), name='content-retrieve-update-destroy'),
# ]

from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    ContentListCreateAPIView,
    ContentRetrieveUpdateDestroyAPIView,
    ContentArchiveAPIView,  # Import the new view for archiving content
    ArchivedContentListAPIView,
    ContentUnarchiveAPIView,
    ContentRestoreAPIView,
    ContentSoftDeleteAPIView
)

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('contents/', ContentListCreateAPIView.as_view(), name='content-list-create'),
    path('contents/<int:pk>/', ContentRetrieveUpdateDestroyAPIView.as_view(), name='content-retrieve-update-destroy'),
    path('contents/<int:pk>/archive/', ContentArchiveAPIView.as_view(), name='content-archive'),  # URL for archiving content
     path('contents/archived/', ArchivedContentListAPIView.as_view(), name='archived-content-list'),  # URL for retrieving archived content
     path('contents/<int:pk>/unarchive/', ContentUnarchiveAPIView.as_view(), name='content-unarchive'),
     path('contents/<int:pk>/soft-delete/', ContentSoftDeleteAPIView.as_view(), name='content-soft-delete'),  # URL for soft deletion
     path('contents/<int:pk>/restore/', ContentRestoreAPIView.as_view(), name='content-restore'),  # URL for restoring soft-deleted content
]
