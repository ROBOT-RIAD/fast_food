from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemListView,ItemDetailView,ReviewViewset


router = DefaultRouter()
router.register("reviews",ReviewViewset)
router.register("all",ItemListView)


urlpatterns = [
    path('', include(router.urls)),
    path('all/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]
