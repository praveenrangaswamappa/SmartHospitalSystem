from django.shortcuts import render_to_response, RequestContext
from django.db.models import Q 
from django.contrib.auth.decorators import login_required

from apps.patient.models import Patient
from apss.reports.forms import SearchForm

@login_required()
def patientview(request):
    patients=[]
    query=[]
    if request.method=="POST":
        searchform=SearchForm(request.POST)
        query = searchform.data['query']
        if query:
            qset = (
                    Q(patientname__icontains=query) |
                    Q(patientid__icontains=query)
            )
            patients = Patient.objects.filter(qset).distinct()
            
        else:
            patients = Patient.objects.order_by('patientname')
            
    #patients = Patient.objects.order_by('-patientname')
    
    searchform=SearchForm()
    return render_to_response("patient.html",{"patients":patients,"searchform":searchform,"query":query},context_instance=RequestContext(request))

