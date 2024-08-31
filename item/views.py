from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Item,Review
from .serializers import ItemSerializer,ReviewSerializer
from django.views.generic import CreateView
from django.urls import reverse_lazy
from item.forms import ItemForm
from rest_framework import viewsets,filters

# Create your views here.

class ItemListView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends =[filters.SearchFilter]
    search_fields =['title']

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemCreateView(CreateView):
    model =Item
    form_class =ItemForm
    template_name = 'item.html'
    success_url = reverse_lazy('item-create')
    def form_valid(self, form):
        return super().form_valid(form)
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer