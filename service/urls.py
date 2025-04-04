from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('service', views.ServiceViewset)
router.register('prescription', views.PrescriptionViewset) 
router.register('bed', views.BedViewset) 
router.register('emergency', views.EmergencyCaseViewset) 
router.register('invoice', views.InvoiceViewset) # router er antena
urlpatterns = [
    path('', include(router.urls)),
]