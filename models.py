from django.db import models

# Create your models here.

class Invoice(models.Model):
    date= models.DateField()
    invoice_No = models.IntegerField()
    customer_Name = models.CharField(max_length=30)
    

class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='details')
    description=models.CharField(max_length=40)
    quantity=models.IntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2)


    
    