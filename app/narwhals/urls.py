# todos/urls.py
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/patients', PatientViewSet, 'patients')
router.register('api/doctors', DoctorViewSet, 'doctors')
# router.register('api/patientsImages', PatientImageViewSet, 'patientsImages')
router.register('api/pathologyScan', PathologyImageScanView, 'pathologyScan')

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
     path('api/gcpImages/<int:pk>/', GCPImage.as_view()),
     path('sentry-debug/', trigger_error),
     # path('api/pathologyScan/<int:pk>/', PathologyImageScanView.as_view()),
]

urlpatterns += router.urls

