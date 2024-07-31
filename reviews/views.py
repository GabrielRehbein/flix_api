from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from core.permissions import GlobalDefaultPermission

class ReviewsListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewsDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer