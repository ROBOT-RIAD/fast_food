from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,AddMoneyView,BalanceView,ActivateUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add_money/', AddMoneyView.as_view(), name='add-money'),
    path('balance/', BalanceView.as_view(), name='user-balance'),
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),
]
