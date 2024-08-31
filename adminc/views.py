from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from burger.models import Order
from datetime import datetime
from django.db.models import Sum

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()  # Get the logged-in user
        if user.is_superuser:
            messages.success(self.request, "Login successful")
            return super().form_valid(form)
        else:
            messages.error(self.request, "You are not authorized to access this page")
            return HttpResponseRedirect(reverse_lazy('login'))  # Redirect back to the login page


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login') 
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated:
                logout(self.request)
            return redirect(self.next_page)
        else:
            return super().dispatch(request, *args, **kwargs)
        


class UnpaidOrderView(ListView):
    model = Order
    template_name = 'unpaid.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(payment=False)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        total_price = queryset.aggregate(total_price=Sum('price'))['total_price']
        context['total_price'] = total_price
        return context