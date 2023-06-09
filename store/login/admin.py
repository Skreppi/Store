from django.contrib import admin

from login.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration', ]
    fields = ['code', 'user', 'expiration', 'created']
    readonly_fields = ('created',)
