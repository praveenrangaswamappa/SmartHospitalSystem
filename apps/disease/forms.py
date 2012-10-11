from django import forms

from apps.prescription.models import Prescription,Disease

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
#        fields = ('patientid','drugname')
class diseaseForm(forms.ModelForm):
    class Meta:
        model=Disease