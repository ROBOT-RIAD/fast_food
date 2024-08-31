from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryListView


router = DefaultRouter()



urlpatterns = [
    path('', include(router.urls)),
    path('all/', GalleryListView.as_view(), name='item-list'),
]
