from django.contrib import admin

from services.models import Service, Plan, Subscription

admin.site.register(Plan)
admin.site.register(Service)
admin.site.register(Subscription)
