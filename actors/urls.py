from django.urls import path

from actors.views import ActorListCreateView, ActorDetailUpdateDeleteView

urlpatterns = [


    path('actors/', ActorListCreateView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorDetailUpdateDeleteView.as_view(), name='actor-detail-update-delete-view'),
]
