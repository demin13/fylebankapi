from django.db import models

class bankmodel(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField

    class Meta:
        db_table='banks'

class branchmodel(models.Model):
    ifsc = models.CharField(max_length=20, primary_key=True)
    bank_id=models.IntegerField()
    branch=models.CharField(max_length=150)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=50)

    class Meta:
        db_table="branches"
