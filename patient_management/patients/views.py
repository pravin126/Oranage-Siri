from rest_framework import generics
from .models import Patient, FamilyMember, Medication
from .serializers import PatientSerializer, FamilyMemberSerializer, MedicationSerializer, Patient360Serializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class Patient360View(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = Patient360Serializer

class FamilyMemberListCreateView(generics.ListCreateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class FamilyMemberDetailView(generics.RetrieveUpdateAPIView):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class MedicationListCreateView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedicationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

