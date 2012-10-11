from django import forms

from apps.invoice.models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
                
        

#class BillingForm(forms.Form):
#    """Patient billing form"""
#    patientname = forms.CharField(max_length = 30, widget=forms.Textarea)
##    dateofbirth = forms.DateField(initial = datetime.date.today())
##    dateofbirth = forms.DateField(input_formats = "%d/%m/%yyyy")
#    age         = forms.IntegerField()
#    sex         = forms.CharField(max_length = 1 , help_text = "M/F")
#    phonenumber = forms.IntegerField()
#    email       = forms.EmailField()
#    
#    def clean_name(self):
#        """function for getting clean data of field name"""
#        data = self.cleaned_data['patientname']
#        if "pavi" in data :
#            return data
#        else:
#            raise forms.ValidationError("Enter proper name")
#    
#    def clean(self):
#        data = self.cleaned_data['email']
#        if "pavi" in  data:
#            return data
#        raise forms.ValidationError("Enter proper email address ex:username@example.com")
#
#class ContactForm(forms.Form):
#    email = forms.EmailField()
#    
#    def clean(self):
#        data = self.cleaned_data['email']
#        if "pavi" in  data:
#            return data
#        raise forms.ValidationError("Enter proper email address")
