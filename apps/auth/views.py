from django.shortcuts import render_to_response, HttpResponse, RequestContext

#---User Authentication----
from django.contrib.auth import authenticate, login, logout

from apps.auth.forms import LoginForm
from apps.patientregistration.forms import PatientRegistrationForm

#######################################################################
#Name: loginview()                                                    #
#Description: Used for authenticating user                            #
#Function Calls: None                                                 #
#Input(s): request                                                    #
#Output(s): Http response.                                            #
#######################################################################
def loginview(request):
    if request.method == "POST":
        loginform = LoginForm(request.POST)

        username = loginform.data['username']
        password = loginform.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
#                patientregistrationform = PatientRegistrationForm()
                return render_to_response("home.html",context_instance=RequestContext(request))
#                HttpResponse("<html><body>Successfull login</body></html>")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("<html><body>Account is disabled</body></html>")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("<html><body>Unable to login</body></html>")
    #default page for rendering when /bill is loaded for first time
    loginform = LoginForm()
    return render_to_response('login.html',{'loginform':loginform,},context_instance=RequestContext(request))


def logoutview(request):
    logout(request)
    return render_to_response("logout.html",context_instance=RequestContext(request))

