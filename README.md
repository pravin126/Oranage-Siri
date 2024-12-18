# Oranage-Siri

Overview

This assessment is designed to evaluate your proficiency in building and working with Django applications, including defining models, creating REST APIs using Django REST framework, and developing core backend logic to serve a business use case.

Building the Core Application

Objective

Create a Django application for managing patient information.

Problem Statement

You are tasked with building a basic Patient Management Module with the following requirements:

Requirements

1. Patient

a. A Django Model to represent a patient with details like name, date of birth, gender and all such relevant fields.

b. REST APIs to -

i. Create a patient

ii. List all patients

iii. Retrieve a given patient

iv. Update a given patient

2. Patient Family Members

a. A Django Model to represent the family members of a patient with details which patient is related to which other patient and by what relation

b. REST APIs to -

i. Add a family member for a patient

ii. List all family members of a given patient

iii. Retrieve a given family member of a given patient

iv. Update a particular family member with details for example updating a relation from fiancé to spouse

3. Medications

a. A Django Model to represent the medications prescribed to a particular patient along with details like dosage, timings and other relevant details

b. REST APIs to -

i. Add an active medication for a patient

ii. List all active medications for a given patient

iii. Retrieve a given medication for a patient

iv. Activate or deactivate certain medication(s) for a given patient

v. Increase or decrease Medication Dosage, alter timings or update any such medication information for a Medication prescribed for a patient

4. Patient 360

a. REST APIs to -

i. Get the entire Patient 360: Given a patient ID, get all the demographics data of the patient along with the entire family of the patient and the emergency contacts as well

ii. Update the patient 360: Given a patient ID, expose a REST API to update either the patient demographics data, or any family member or any of the patient’s emergency contacts.

Instructions

1. Models (DB) Design:

a. Design appropriate models in Django along with relationships between the models wherever applicable

b. Include constraints, indexes, default values, choices etc. wherever applicable.

2. API Design and Development

a. Use standard RESTful conventions for API endpoints.

b. Implement meaningful status codes and error messages.

c. Use standard Django and Django REST Framework for implementation of REST APIs. For example:

i. Use of Generic API View Classes

ii. Use of Model Serializers (Nested or simple) in the APIs


Endpoints
Create a Patient: POST /api/patients/
Retrieve Patient 360: GET /api/patients/<id>/360/
Add a Family Member: POST /api/family-members/
Add Medication: POST /api/medications/


