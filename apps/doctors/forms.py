from django import forms

from apps.prescription.models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
#        fields = ('patientid','drugname')