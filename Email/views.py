from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Email
from .serializers import EmailSerializer
from django.views.generic import ListView
from datetime import datetime

# Create your views here.
class EmailCreateView(CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailListView(ListView):
    model = Email
    template_name = 'email.html'
    context_object_name = 'email_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            queryset = queryset.filter(time__date__gte=start_date, time__date__lte=end_date)
        return queryset

