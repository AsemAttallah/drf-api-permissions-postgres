from django.urls import path
from .views import CarListView, CarDetailView, PostListView, PostDetailView
urlpatterns = [
    path('',CarListView.as_view(),name='car_list'),
    path('<int:pk>/',CarDetailView.as_view(),name='car_detail'),
    path('post/',PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
]
