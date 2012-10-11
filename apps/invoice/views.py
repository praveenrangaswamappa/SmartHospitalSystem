from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django.db import transaction
from apps.patientregistration.models import PatientMaster
from apps.invoice.models import Invoice
from django.db.models import Sum
import datetime
from apps.pharmacy.models import Pharmacy
from apps.invoice.forms import InvoiceForm
from apps.prescription.models import Prescription
 
@login_required()
def invoiceview(request): 
    query = request.POST.get('search')
    
    if query:
        
        patients = PatientMaster.objects.filter(patientid__iexact=query).distinct() 
        objInvoice = PatientMaster.objects.all()
        idd=len(objInvoice)+1
        invoiceid='Invoice_No-'+str(idd) 
        date=datetime.datetime.now()
        results =  Pharmacy.objects.values("prescription__drugname","prescription__patientid","prescription__qty","prescription__qty","price").annotate(totalqty = Sum("prescription__qty"))
        for item in results:
            item['totalprice'] = item["totalqty"] * item["price"]
        totalpharmacycost = 0    
        for item in results:
            totalpharmacycost += item['totalprice']
        
#    if request.method == "POST":
#        form = InvoiceForm(request.POST)
#        if form.is_valid():
#            with transaction.commit_on_success():
#                 form.save()
    else:
        patients = [] 
        date=[]   
        invoiceid=[]
        results=[]
        totalpharmacycost = 0
    return render_to_response("invoice.html",{"patients":patients,"date":date,"invoiceid":invoiceid,"results":results, "totalpharmacycost":totalpharmacycost},context_instance=RequestContext(request))
