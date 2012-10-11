from django import forms
from django.forms import ModelForm, Textarea,TextInput

from apps.patientregistration.models import PatientMaster,PatientContact

    
class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = PatientMaster
        fields=('patientcategory','pre','fastname','middlename','lastname','parentname','sex','dateofbirth','age','bloodgroup','diseasename','subcategory')
#        widgets={'middlename':TextInput(attrs={'size':'8'})
#                                 }
         
class PatientContactForm(forms.ModelForm):
    class Meta:
        model=PatientContact
        fields=('address','zip','phonenumber','email','city','state')
        widgets = {
            'address': Textarea(attrs={'cols': 22, 'rows':6}),
        }
         
           
#class PatientRegistrationFormm(forms.ModelForm):
#    class Meta:
#        model = Patientt
##        fields = ('patientname', 'patientlastname')
#    def __init__(self, *args, **kwargs):
#        super(PatientRegistrationFormm, self).__init__(*args, **kwargs)
#        self.fields['patientname'].label = 'First Name'
#        self.fields['patientlastname'].label = 'Last Name'