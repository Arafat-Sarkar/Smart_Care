from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
        fields = '__all__'
        
class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bed
        fields = '__all__'
        
class EmergencyCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmergencyCase
        fields = '__all__'
        
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'