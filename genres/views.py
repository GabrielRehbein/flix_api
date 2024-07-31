from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from core.permissions import GlobalDefaultPermission




class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    