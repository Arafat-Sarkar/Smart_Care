from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length= 30)
    phone = models.CharField(max_length= 15)
    problem = models.TextField()
    
    def __str__(self):
        return self.name
    
    
     