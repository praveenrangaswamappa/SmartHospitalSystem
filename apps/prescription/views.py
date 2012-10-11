from django.shortcuts import render_to_response, RequestContext
from django.db import transaction  
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


from apps.patient.models import Patient
from apps.patientregistration.models import PatientMaster
from apps.prescription.models import Prescription
from apps.prescription.forms import PrescriptionForm
from django.db.models import Sum 

@login_required()                 
def prescriptionview(request):
#    patient = Patient.objects.values("patientid")
    prescriptiongiven = Patient.objects.values("patientid" ,"prescription__dosage",  "prescription__drugname", "prescription__when" , "prescription__units" ).annotate(totalqty = Sum("prescription__qty"))
#    prescriptiongiven = Prescription.objects.values("dosage","drugname","when","units").annotate(totalqty = Sum("qty"))
#    prescriptiongiven = Prescription.objects.select_related().annotate(totalqty = Sum("qty"))
    
    form = PrescriptionForm() 
    
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            with transaction.commit_on_success():
                 form.save()
                 
    
               
    if prescriptiongiven:
            return render_to_response("prescription.html",{"form":form,"prescriptiongiven":prescriptiongiven},context_instance=RequestContext(request))
            
    else:  
            return render_to_response("prescription.html",{"form":form},context_instance=RequestContext(request))

@login_required()
def prescriptiongivenview(request):
    prescriptiongiven = Prescription.objects.all()
    return render_to_response("prescriptiongiven.html",{"prescriptiongiven":prescriptiongiven},context_instance=RequestContext(request))

