from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from rest_framework import status
from .serializers import UserSerializer,AddMoneySerializer,AddMoneyViewSerializer
from rest_framework.permissions import IsAuthenticated


from  django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(user,subject,amount,total,template):
    message = render_to_string(template,{'user': user,'total':total,'amount':amount})
    send_email =EmailMultiAlternatives(subject,"",to =[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =UserSerializer
       



class AddMoneyView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AddMoneySerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            amount = serializer.validated_data.get('balance', 0)
            user.balance += amount
            subject = 'Your add money Has Been Successful'
            template = 'add_money_email.html'
            send_email(user,subject,amount,user.balance,template)
            user.save()
            return Response({'status': 'balance updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 





class BalanceView(APIView):
   
    def get(self, request):
        user = request.user  
        serializer = AddMoneySerializer(user)
        return Response(serializer.data)