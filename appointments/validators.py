from django.core.exceptions import ValidationError
from django.utils import timezone


# Validaciones personalizadas
def validate_not_past(date):
    if date < timezone.now().date():
        raise ValidationError("La fecha no puede estar en el pasado.")

def validate_positive(value):
    if value <= 0:
        raise ValidationError("El valor debe ser positivo.")
