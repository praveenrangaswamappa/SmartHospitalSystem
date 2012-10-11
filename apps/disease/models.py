from django.db import models

class Disease(models.Model):
    diseasename = models.CharField(max_length = 40, primary_key=True)
    rate = models.FloatField(max_length = 20, blank = True, null = True)
    def __unicode__(self):
        return self.diseasename
    
class Category(models.Model):
    #diseasename = models.CharField(max_length = 40)
    diseasename = models.ForeignKey(Disease)
    subcategory = models.CharField(max_length = 40)
    rate_for_NABH   = models.FloatField(max_length = 20, blank=True, null=True)
    rate_for_non_NABH =models.FloatField(max_length = 20, blank=True, null=True)
    rate_for_superspecial = models.FloatField(max_length = 20, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s"%(self.subcategory)
