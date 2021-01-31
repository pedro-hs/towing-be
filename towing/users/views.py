from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from utils import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = User

    def get_permissions(self):
        self.permission_classes = (IsAdminUser,)

        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.Meta.model(**serializer.data)
        password = request.data['password']
        instance.set_password(password)
        instance.save()

        data = UserSerializer(instance).data
        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_update(self, serializer):
        if serializer.validated_data.get('role', 'user') == 'admin':
            serializer.validated_data['is_staff'] = True

        serializer.save()

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PasswordResetView:
    @ receiver(reset_password_token_created)
    def send_email(instance, reset_password_token, *args, **kwargs):
        host_url = instance.request.get_host()
        site_url = (host_url if host_url in settings.CORS_ORIGIN_WHITELIST
                    else settings.CORS_ORIGIN_WHITELIST[0])
        link = f'{site_url}/auth/change-password/{reset_password_token.user.email}/{reset_password_token.key}'

        subject = 'Password reset'
        message = f'Click on link to create a new password. {link}'
        from_ = settings.EMAIL_HOST_USER
        to_ = (reset_password_token.user.email,)

        send_mail(subject, message, from_, to_)
