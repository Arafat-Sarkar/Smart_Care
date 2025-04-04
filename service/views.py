from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    
    
class PrescriptionViewset(viewsets.ModelViewSet):
    queryset = models.Prescription.objects.all()
    serializer_class = serializers.PrescriptionSerializer
    
class BedViewset(viewsets.ModelViewSet):
    queryset = models.Bed.objects.all()
    serializer_class = serializers.BedSerializer
    
class EmergencyCaseViewset(viewsets.ModelViewSet):
    queryset = models.EmergencyCase.objects.all()
    serializer_class = serializers.EmergencyCaseSerializer
    
class InvoiceViewset(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer