from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True,required=True,style={'input_type':"password"})
    class Meta:
        model = User
        fields = ['id','email','password']

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        user = User.objects.Create_user(email,password)
        user.is_active = False
        user.save()
        self.send_confirmation_email(user)
        return user
    def send_confirmation_email(self, user):
        from django.core.mail import EmailMultiAlternatives
        from django.template.loader import render_to_string
        from django.utils.http import urlsafe_base64_encode
        from django.utils.encoding import force_bytes
        from django.contrib.auth.tokens import default_token_generator

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        confirm_link = f"https://fast-food-nzvp.onrender.com/account/activate/{uid}/{token}"
        email_subject = "Confirm your Email"
        email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()
    


class AddMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['balance']

class AddMoneyViewSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['balance']
        