from django.db import models


# Create your models here.
class Admin(models.Model):
    id: models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)

    # name of the table in database not specified
    class Meta:
        db_table = "ttmadmin_table"

class Register(models.Model):
    id: models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=25, blank=False, unique=True)
    phno = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)


    class Meta:
        db_table="register_table"