from django.db import models

class Invoice(models.Model):
    AMB_OPTION = { ("Y","Yes"),("N","NO")}
    INS_OPTION = { ("Y","Yes"),("N","NO")}
    patientid = models.CharField("Patient ID",max_length = 10)
    patientname = models.CharField("Patient Name",max_length = 15)
    invoicenumber = models.CharField("Invoie Number",max_length = 10)
    taxnumber  = models.CharField("Tax Number",max_length = 10)
    billid = models.CharField("Bill ID",max_length = 10)
    dateofjoining = models.DateField("DateOfJoining")
    dateofdisharge = models.DateField("DateOfDischarge")
    #presrciption = models.CharField()
    pharmacycharges = models.FloatField("Pharmacy Charges",max_length = 6)
    bedcharges = models.FloatField("Bed Charges",max_length =6)
    insurancepolicyno = models.FloatField("Insurance Policy Number",max_length = 6)
    insuranceprovider = models.CharField("Insurance Provider",max_length = 15)
    insuranceProcessingfee = models.FloatField("Insurance Proessing FEE",max_length = 6,choices=INS_OPTION)
    miscellaneous = models.FloatField("Miscellaneous ",max_length = 6)
    insuranceclaims = models.FloatField("Insurance Claims",max_length = 6)
    ambulance = models.CharField("Ambulance",max_length = 1,choices =AMB_OPTION)
    doctorconsultationfee = models.FloatField("Doctor Consulting FEE",max_length =6)
    
    def __unicode__(self):
        return "%s"%(self.invoicenumber)
    
    