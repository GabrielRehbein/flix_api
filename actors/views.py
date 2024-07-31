from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer
from core.permissions import GlobalDefaultPermission

class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer