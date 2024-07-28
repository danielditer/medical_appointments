from rest_framework import viewsets, status
from .models import Patient, Doctor, Appointment, Prescription
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, PrescriptionSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

@api_view(['GET'])
def filter_prescriptions_by_patient_first_name(request, first_name):
    if first_name:
        prescriptions = Prescription.objects.filter(appointment__patient__first_name=first_name)
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'El nombre es requerido'}, status=status.HTTP_400_BAD_REQUEST)
