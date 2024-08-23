from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class =OrderSerializer
    permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        queryset = Order.objects.all()
        id = self.request.query_params.get("id",None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        # user = self.request.user
        # queryset = queryset.filter(user__id=user.id)
        return queryset

