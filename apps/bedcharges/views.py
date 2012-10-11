# Create your views here.
from django.shortcuts import render_to_response, RequestContext
from django.db import transaction
from django.contrib.auth.decorators import login_required


from apps.bedcharges.forms import bedForm
from apps.bedcharges.models import bed

@login_required()        
def bedview(request):
    if request.method == "POST":
        bedform  = bedForm(request.POST)
        if bedform.is_valid():
            with transaction.commit_on_success():
                  bedform.save()
    form = bedForm()
    return render_to_response("bed.html",{"form":form},context_instance=RequestContext(request))
                 