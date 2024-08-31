from django.shortcuts import render
from django.views.generic import ListView
from burger.models import Order
from datetime import datetime
from django.db.models import Sum

class homeView(ListView):
    model = Order
    template_name = 'index.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            queryset = queryset.filter(orderTime__date__gte=start_date, orderTime__date__lte=end_date)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        total_price = queryset.aggregate(total_price=Sum('price'))['total_price']
        context['total_price'] = total_price
        return context
