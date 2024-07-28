from django.contrib import admin

from appointments.models import Patient, Doctor, Prescription, Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Prescription)