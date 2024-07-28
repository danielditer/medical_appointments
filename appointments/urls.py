from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet, PrescriptionViewSet, filter_prescriptions_by_patient_first_name

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('prescriptions/filter-by-patient-first-name/<str:first_name>/', filter_prescriptions_by_patient_first_name, name='filter-prescriptions-by-patient-first-name'),
]
