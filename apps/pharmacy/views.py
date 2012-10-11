from django.shortcuts import render_to_response, RequestContext
from django.db import transaction

from apps.pharmacy.forms import PharmacyForm

def pharmacyview(request):
    
    if request.method == "POST":
        form = PharmacyForm(request.POST)
        if form.is_valid():
            with transaction.commit_on_success():
                 form.save()
                 
    form = PharmacyForm()
    return render_to_response("pharmacy.html",{"form":form},context_instance=RequestContext(request))
