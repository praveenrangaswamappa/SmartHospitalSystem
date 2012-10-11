from django.shortcuts import render_to_response, RequestContext
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.patientregistration.forms import PatientRegistrationForm,PatientContactForm
from apps.patientregistration.models import PatientMaster,PatientContact

@login_required()        
def patientregistrationview(request):
    """bill view"""
    if request.method == "POST":
        
        patientregistrationform  = PatientRegistrationForm(request.POST)
        patientcontactform       = PatientContactForm(request.POST)
        if patientcontactform.is_valid()and patientregistrationform.is_valid():
            with transaction.commit_on_success():
                 
                 idd=len(PatientMaster.objects.all())+1
                 patient='HSP'+str(idd)
                 new_user = patientregistrationform.save(commit=False)
                # blood=patientregistrationform.data['lastname']
                 new_user.patientid=patient
                 new_user.save()
            with transaction.commit_on_success():
                 conct= patientcontactform.save(commit=False);
                
                 conct.contactid=patient
                 conct.save()
            patients = PatientMaster.objects.order_by('patientid')
            contact  = PatientContact.objects.all()
            return render_to_response("patient.html",{"patients":patients,"contact":contact,}, context_instance=RequestContext(request))
        else:
            #redirects to bill.html with error in form
            return render_to_response('patientregistration.html',{'patientregistrationform':patientregistrationform,'patientcontactform':patientcontactform,},context_instance=RequestContext(request))

   # default page for rendering when /bill is loaded for first time
    patientregistrationform = PatientRegistrationForm()
    patientcontactform      = PatientContactForm()
    return render_to_response('patientregistration.html',{'patientregistrationform':patientregistrationform,'patientcontactform':patientcontactform,},context_instance=RequestContext(request))
