from django.urls import path
from .views import EmailCreateView

urlpatterns = [
    path('', EmailCreateView.as_view(), name='email-create'),
]
