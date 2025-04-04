from django.db import models
from patient.models import Patient
from doctor.models import Doctor

class Service(models.Model):
    name = models.CharField(max_length= 30)
    description = models.TextField()
    image = models.ImageField(upload_to= "sevice/images/")



class Prescription(models.Model):
    patient = models.ForeignKey( Patient , on_delete=models.CASCADE)
    doctor = models.ForeignKey( Doctor , on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    prescribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.name}"
    
    
class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='invoices')
    invoice_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        status = "Paid" if self.is_paid else "Outstanding"
        return f"Invoice {self.id} for {self.patient.user.username} - {status}"
    
    
class EmergencyCase(models.Model):
    patient = models.ForeignKey( Patient , on_delete=models.CASCADE)
    severity = models.CharField(max_length=50, choices=[('Critical', 'Critical'), ('Moderate', 'Moderate'), ('Mild', 'Mild')])
    description = models.TextField()
    admission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency Case of {self.patient.name} - {self.severity}"

class Bed(models.Model):
    bed_number = models.CharField(max_length=20, unique=True)
    is_occupied = models.BooleanField(default=False)
    patient = models.ForeignKey( Patient , on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Bed {self.bed_number} - {'Occupied' if self.is_occupied else 'Available'}"


