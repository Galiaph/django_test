from django.contrib import admin
from .models import *

class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    class Meta:
        model = Subscriber
    
admin.site.register(Subscriber, SubscribersAdmin)
