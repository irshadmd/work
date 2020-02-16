from django.db import models
import datetime
# Create your models here.
class operator_attendence(models.Model):
    operator_id = models.CharField(max_length=5,default='')
    operator_name = models.CharField(max_length=50,default='')
    date= models.DateField(default=datetime.date.today)
    attendence=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.operator_name
