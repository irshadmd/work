from django.shortcuts import render
from authenticate.forms import UserForm,windowForm
from authenticate.models import UserProfileInfo,OperatorWindow
from attendence.models import operator_attendence
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import sqlite3
from datetime import date

def index(request):
    return render(request,'authenticate/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
    return render(request,'authenticate/index.html')

def takeattendence(request):
    context={}
    operator_list=UserProfileInfo.objects.all()
    context['operator_list']=operator_list
    return render(request,'authenticate/takeattendence.html',context)

def submitattendence(request):
    operators=UserProfileInfo.objects.all()
    attenddatescheck=operator_attendence.objects.all()
    today = str(date.today())
    c=0
    for check in attenddatescheck:
        if(str(check.date)==today):
            c=1
    if(c==0):
        for i in operators:
            attend=request.POST[i.operator_id]
            operatorAttend=operator_attendence(operator_id=i.operator_id,operator_name=i.operator_name
            ,attendence=attend)
            operatorAttend.save()
            print(attend)
        return HttpResponse("Attendence submitted")
    else:
        return HttpResponse("Already submitted")

def takeleave(request):
    return render(request,'authenticate/takeleave.html')

def leavesubmit(request):
    id=request.POST['operatorid']
    leavestart=request.POST['leavestart']
    leaveend=request.POST['leaveend']
    operators=operator_attendence.objects.all()
    c=0
    today = str(date.today())
    for i in operators:
        if(id==i.operator_id and today==str(i.date)):
            if(i.leave=='on leave'):
                mess="Already on leave"
                return render(request,'authenticate/takeleave.html',{'mess':mess})
            else:
                c=1
                i.attendence='absent'
                i.leave='on leave'
                i.leave_start=leavestart
                i.leave_end=leaveend
                i.save()
    if(c==0):
        mess="Enter valid Operator id"
        return render(request,'authenticate/takeleave.html',{'mess':mess})
    print(leavestart,leaveend)
    return HttpResponse("Submited")
