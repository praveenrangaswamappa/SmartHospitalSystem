from django.db import models



class Pharmacy(models.Model):
    drugname = models.CharField(max_length = 40,primary_key = True)
    price  = models.FloatField(max_length = 5)
    qty    = models.PositiveSmallIntegerField(max_length = 4)
    
    def __unicode__(self):
        return self.drugname
