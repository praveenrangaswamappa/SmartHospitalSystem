from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from apps.patientregistration.models import PatientMaster,PatientContact


@login_required()
def patientview(request):
#    patients = PatientMaster.objects.order_by('patientid') 
#    contact  = PatientContact.objects.all()
    query = request.POST.get('search')
    if query:
        qset = (
                Q(patientid__iexact=query)
               )
        patients = PatientMaster.objects.filter(qset).distinct()
        contact=PatientContact.objects.filter(contactid=query)
    else:
        patients = []
        contact=[]
    return render_to_response("patient.html",{"patients":patients,"contact":contact}, context_instance=RequestContext(request))
