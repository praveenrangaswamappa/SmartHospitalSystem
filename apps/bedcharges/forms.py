from django import forms

from apps.bedcharges.models import bed

class bedForm(forms.ModelForm):
    class Meta:
        model = bed
#        fields = ('patientid','drugname')