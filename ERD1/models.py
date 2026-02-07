from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth")

    def __str__(self):
        return self.name

class Appointment(models.Model):
    # This creates the Foreign Key links from the ERD
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="Scheduled")

    def __str__(self):
        return f"{self.patient} with {self.doctor} at {self.appointment_time}"