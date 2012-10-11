from django.db import models

from apps.patient.models import Patient
from apps.pharmacy.models import Pharmacy

class Prescription(models.Model):
    DOSAGE_CHOICES  = { ("1-0-0","Morning one"), ("0-0-1","Afternoon one"), ("0-0-1","Evening one"),
                        ("1-0-1","Morning and evening"), ("1-1-0","Morning and afternoon"), ("0-1-1","Afternoon and Night"),
                        ("1-1-1","All three times")}
    
    WHEN_CHOICES = {('b','before food',),('a','after food',)}
    UNITS_CHOICES = {('ml', 'Mililiter'),('Tab', "Tablet")}
#    rate at which to be given --aplicable for glucose or sodium drips
    patientid = models.ForeignKey(Patient)
    drugname = models.ForeignKey(Pharmacy)
    qty    = models.PositiveSmallIntegerField(max_length = 4)
    dosage = models.CharField(max_length = 5, choices = DOSAGE_CHOICES)
    when =     models.CharField(max_length = 11, choices = WHEN_CHOICES)
    units = models.CharField(max_length = 3,choices = UNITS_CHOICES)
    
    def __unicode__(self):
       return "%s,%s,%s"%(self.patientid, self.drugname)
