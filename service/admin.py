from django.contrib import admin

from .import models

admin.site.register(models.Service)
admin.site.register(models.Bed)
admin.site.register(models.EmergencyCase)
admin.site.register(models.Invoice)
admin.site.register(models.Prescription)
