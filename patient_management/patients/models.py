from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class FamilyMember(models.Model):
    RELATIONSHIP_CHOICES = [
        ('Parent', 'Parent'),
        ('Sibling', 'Sibling'),
        ('Child', 'Child'),
        ('Spouse', 'Spouse'),
        ('Other', 'Other'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='family_members')
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.name} ({self.relation})"


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medications')
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
