from django.urls import path,include
from core.views import homeView
from Email.views import EmailListView
from Gallery.views import GalaryCreateView
from item.views import ItemCreateView
from burger.views import OrderUpdateView
from .views import UserLoginView,UserLogoutView,UnpaidOrderView
urlpatterns = [
    path('',UserLoginView.as_view(),name='login'),
    path('home/',homeView.as_view(),name ='home'),
    path('email/',EmailListView.as_view(),name ='email'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('Unpaid-order/',UnpaidOrderView.as_view(),name='unpaidorder'),
    path('gallery/create/',GalaryCreateView.as_view(), name='gallery-create'),
    path('item/create/',ItemCreateView.as_view(), name='item-create'),
    path('editorder/<int:id>/', OrderUpdateView.as_view(), name='edit_Order'),
]
