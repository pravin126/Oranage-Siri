from django.urls import path
from . import views

urlpatterns = [
    # Patient APIs
    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patients/<int:pk>/360/', views.Patient360View.as_view(), name='patient-360'),

    # Family Member APIs
    path('family-members/', views.FamilyMemberListCreateView.as_view(), name='family-member-list-create'),
    path('family-members/<int:pk>/', views.FamilyMemberDetailView.as_view(), name='family-member-detail'),

    # Medication APIs
    path('medications/', views.MedicationListCreateView.as_view(), name='medication-list-create'),
    path('medications/<int:pk>/', views.MedicationDetailView.as_view(), name='medication-detail'),
]
