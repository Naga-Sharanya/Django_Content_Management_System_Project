# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import TicketSerializer
# from category.models import Category  # Import the Category model

# class TicketCreateAPIView(APIView):
#     def post(self, request, format=None):
#         # Retrieve the category data from the request
#         category_name = request.data.get('category')

#         # Check if the category exists in the database
#         try:
#             category = Category.objects.get(name=category_name)
#         except Category.DoesNotExist:
#             # Handle the case where the category doesn't exist
#             return Response({"error": f"Category '{category_name}' does not exist."}, status=status.HTTP_400_BAD_REQUEST)

#         # Create the serializer with the validated category instance
#         serializer = TicketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(category=category)  # Assign the category instance to the serializer
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer

class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer