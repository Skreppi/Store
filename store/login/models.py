from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)

    def get_success_url(self):
        return redirect("profile" + '/' + self.user.pk)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return self.user.email

    def send_verification_email(self):
        link = reverse('email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'http://127.0.0.1:8000{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = f'Для подтверждения учетной записи перейдите по ссылке: {verification_link}'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [self.user.email],
            fail_silently=False
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
