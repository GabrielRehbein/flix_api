from django.urls import path

from reviews.views import ReviewsListCreateView, ReviewsDetailUpdateDeleteView

urlpatterns = [

    path('reviews/', ReviewsListCreateView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>/', ReviewsDetailUpdateDeleteView.as_view(), name='reviews-detail-update-delete-view'),

]
