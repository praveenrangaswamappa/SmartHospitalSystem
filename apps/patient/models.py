 
#Django Models
from django.db import models

#---SmartHospital System-------
from apps.disease.models import  Disease, Category



"""
    
Usefull links:
-------------

---different fields in models---
1.https://docs.djangoproject.com/en/1.4/ref/models/fields/

----forms.ModelForm---
1.https://docs.djangoproject.com/en/dev/topics/forms/modelforms/
"""

class Patient(models.Model):
    """Class for patient details"""
    SEX_CHOICES  = { ("M","Male"),("F","Female")}
    patientid    = models.AutoField(primary_key=True)
    patientname  = models.CharField(max_length = 30)
    dateofbirth  = models.DateField()
    age          = models.IntegerField()
    sex          = models.CharField(max_length = 1, choices = SEX_CHOICES)
    email        = models.EmailField(null = True, blank = True)
    diseasename  = models.ManyToManyField(Disease, null = True, blank = True)
    subcategory  = models.ManyToManyField(Category, null = True, blank = True)
    phonenumber  = models.IntegerField(max_length=10)
    address      = models.CharField(max_length = 200)
     
    def __unicode__(self):
        return "%s %s"%(self.patientid, self.patientname)
    
class Patientt(models.Model):
    """Class for patient details"""
    SEX_CHOICES  = { ("M","Male"),("F","Female")}
    type         = { ("I","IPD"),("O","OPD"),("E","Emergency")}
    patientid    =  models.AutoField(primary_key=True)
    patientname  = models.CharField(max_length = 30)
    patientlastname= models.CharField(max_length = 30)
    title        = models.CharField(max_length = 6)
    slug         = models.SlugField(unique=True)
    prepopulated_fields={"slug":('patientid',)}
    reg_date     = models.DateField()
    sponsorname  = models.CharField(max_length=30)
    patienttype  = models.CharField(max_length=1, choices=type)
    status       =models.CharField(max_length=15)
    bloodgroup   =models.CharField(max_length=10)
    gender       = models.CharField(max_length = 1, choices = SEX_CHOICES)
    dateofbirth  = models.DateField()
    martialstatus = models.CharField(max_length=15)
    age          = models.IntegerField()
    phonenumber  = models.IntegerField(max_length=10)
    email        = models.EmailField(null = True, blank = True)
    occupation   =models.CharField(max_length =20)
    address      = models.TextField()
    emer_name    = models.CharField(max_length = 30)
    relationship =models.CharField(max_length = 20)
    emer_phonenumber  = models.IntegerField(max_length=12)
    notes      = models.TextField()
#    image     =models.ImageField(upload_to="images") 
        
