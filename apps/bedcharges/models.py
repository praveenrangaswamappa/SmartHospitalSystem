
from django.db import models

class bed(models.Model):
    BED_OPTION = { ("A/C","A/C"),("Non A/C","Non A/C"),("General","General")}
    bedid = models.CharField("Bed ID",max_length = 10)
    bedtype = models.CharField("Bed Type",choices = BED_OPTION, max_length = 10)
    rate = models.FloatField("Rate",max_length = 10)
    