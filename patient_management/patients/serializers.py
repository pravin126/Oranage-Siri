from rest_framework import serializers
from .models import Patient, FamilyMember, Medication

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class Patient360Serializer(serializers.ModelSerializer):
    family_members = FamilyMemberSerializer(many=True, read_only=True)
    medications = MedicationSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'gender', 'phone', 'email', 'address', 'family_members', 'medications']
