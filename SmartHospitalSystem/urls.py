from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from apps.auth.views import loginview, logoutview
from apps.pharmacy.views import pharmacyview
from apps.patientregistration.views import patientregistrationview
from apps.patient.views import patientview
from apps.invoice.views import invoiceview
from apps.prescription.views import prescriptionview, prescriptiongivenview
from apps.bedcharges.views import bedview
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyForms.views.home', name='home'),
    # url(r'^MyForms/', include('MyForms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', loginview),
    url(r'^login/', loginview),
    url(r'^patientregistration/', patientregistrationview),
    url(r'^patient/', patientview),
    url(r'^invoice/', invoiceview),
    url(r'^prescription/', prescriptionview),
    url(r'^prescriptiongiven/', prescriptiongivenview),
#    
    url(r'^logout/', logoutview),
#    
    url(r'^contact/', direct_to_template,{'template':"contact.html"}),
    url(r'^about/', direct_to_template,{'template':"about.html"}),
    url(r'^home/', direct_to_template,{'template':"home.html"}),
    
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': '/path/to/media'}),
    url(r'^pharmacy/', pharmacyview),
    url(r'^bed/', bedview), 
    
    
)
