from django.db import models

class datamodel(models.Model):
    NO=models.IntegerField()
    Challan_Tender_Date=models.DateField()
    Challan_Serial_No=models.IntegerField(unique=True)
    Received_Date=models.DateField()
    Major_Head_Code=models.CharField(max_length=100)
    Minor_Head_Code = models.IntegerField()
    Nature_Of_Payment=models.CharField(max_length=100)
    Status = models.BooleanField()
    Amount=models.FloatField()
