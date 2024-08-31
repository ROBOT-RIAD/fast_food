
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Gallery
from .serializers import GallerySerializer
from django.views.generic import CreateView
from Gallery.forms import GalleryForm
from django.urls import reverse_lazy

# Create your views here.

class GalleryListView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class =  GallerySerializer

class GalaryCreateView(CreateView):
    model =Gallery
    form_class =GalleryForm
    template_name = 'Gallery.html'
    success_url = reverse_lazy('gallery-create')
    def form_valid(self, form):
        return super().form_valid(form)


