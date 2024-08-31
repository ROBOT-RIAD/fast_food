from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Order
from . import forms
from django.urls import reverse_lazy
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import UpdateView
from django.contrib import messages


from  django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(user,subject,total,id,template):
    message = render_to_string(template,{'user': user,'total':total,'id':id})
    send_email =EmailMultiAlternatives(subject,"",to =[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()

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
    

class OrderUpdateView(UpdateView):
    model = Order
    form_class = forms.OrderBuyeUpdate
    template_name = 'ordereidite.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('unpaidorder')

    def form_valid(self, form):
        order = form.instance
        user = order.user
        total = order.price

        if user.balance >= total: 
            user.balance -= total
            user.save()
            order_id = order.id + 10000
            subject = 'Your Order Payment Has Been Successful'
            template = 'payment_email.html'
            send_email(user, subject, total, order_id, template)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Insufficient balance to complete the order.')
            return redirect(self.success_url)

