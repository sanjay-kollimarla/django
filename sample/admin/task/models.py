from django.db import models

# Create your models here.
class Users_Model(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class Tasks_Model(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    title=models.CharField(max_length=20)
    description=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=10)