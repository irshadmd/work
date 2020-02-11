from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    operator_name = models.CharField(max_length=50,default='')
    operator_id = models.CharField(max_length=5,default='')
    address=models.CharField(max_length=100,default='')
    product_category=models.CharField(max_length=100,default='')
    product_sub_category=models.CharField(max_length=100,default='')
    operation=models.CharField(max_length=100,default='')
    operation_complexity=models.CharField(max_length=100,default='')
    no_of_operation=models.CharField(max_length=100,default='')
    skill_percentage=models.CharField(max_length=3,default='')
    grade=models.CharField(max_length=1,default='')
    password = models.CharField(max_length=10,default='')

class OperatorWindow(models.Model):
    operator_id = models.CharField(max_length=5,default='')
    operator_name = models.CharField(max_length=50,default='')
    operation=models.CharField(max_length=100,default='')
    start_time=models.CharField(max_length=50,default='')
    stop_time=models.CharField(max_length=50,default='')
    duration=models.CharField(max_length=50,default='')
    date=models.CharField(max_length=50,default='')
    machine_stop_time=models.CharField(max_length=50,default='')
    machine_run_time=models.CharField(max_length=50,default='')
    machine_breakdown_time=models.CharField(max_length=50,default='')
    frequency_of_machine_stop=models.IntegerField(default=0)
    ticket_no_start=models.IntegerField(default=0)
    ticket_no_end=models.IntegerField(default=0)
    total_pieces=models.IntegerField(default=0)
    ticket_no_run_time=models.IntegerField(default=0)
    next_ticket_no_time=models.IntegerField(default=0)
    ct=models.CharField(max_length=50,default="")
    total_stitched_pieces=models.IntegerField(default=0)
    rework_ticket_no=models.IntegerField(default=0)
    rework_pieces=models.IntegerField(default=0)

def __str__(self):
  return self.operator_name
