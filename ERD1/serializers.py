from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__' 