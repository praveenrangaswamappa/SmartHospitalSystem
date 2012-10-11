from django.db import models
from apps.disease.models import  Disease, Category

class PatientMaster(models.Model):
    SEX_CHOICES          = { ("M","Male"),("F","Female")}
    CATEGORY             = { ("OPD","OPD"),("IPD","IPD")}
    PRE                  = { ("Mr","Mr"),("Mrs","Mrs"),("Miss","Miss")}
    BLOOD_GROUP          = { ("A+","A+"),("B+","B+"),("AB+","AB+"),("O+","O+"),("A-","A-"),("B-","B-"),("O-","O-"),("AB-","AB-")}
    patientid            = models.CharField(unique=True,null = True,max_length = 30)
    patientcategory      = models.CharField("Patient Category",max_length = 3,choices = CATEGORY)
    fastname             = models.CharField("First Name",max_length=25) 
    middlename           = models.CharField("Middle Name",max_length=25)
    pre                  = models.CharField(max_length = 4,choices =PRE)
    lastname             = models.CharField("Last Name",max_length=25)
    parentname           = models.CharField("Father/Husband/Guardian Name",max_length=25)
    sex                  = models.CharField("Sex",max_length =1,choices =SEX_CHOICES)
    diseasename  = models.ManyToManyField(Disease, null = True, blank = True)
    subcategory  = models.ManyToManyField(Category, null = True, blank = True)
    dateofbirth          = models.DateField("Date Of Birth",)
    age                  = models.IntegerField("Age",)
    bloodgroup           = models.CharField("Blood Group",max_length = 3,choices =BLOOD_GROUP,null = True, blank = True)
    
    def __unicode__(self):
        return "%s %s"%(self.patientid, self.fastname )
    
    
class PatientContact(models.Model):
    contactid           = models.CharField(unique=True,null = True,max_length = 30)
    address             = models.CharField("Address",max_length = 50,null=True)
    zip                 = models.IntegerField("Zip",max_length=6,null = True, blank = True)
    phonenumber         = models.IntegerField("Phone No",max_length=10,null = True, blank = True)
    email               = models.EmailField("Email-Id",null = True, blank = True)
    city                = models.CharField(max_length=35,null = True, blank = True)
    state               = models.CharField(max_length=35,null = True, blank = True)
    def __unicode__(self):
        return "%s"%(self.contactid)
