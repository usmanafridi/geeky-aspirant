from django.contrib import admin
from .models import Profile, Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

# Register your models here.
admin.site.register(Profile)
admin.site.register(Subscriber, SubscriberAdmin)