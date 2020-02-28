from django.shortcuts import render
from authenticate.forms import UserForm,windowForm
from authenticate.models import UserProfileInfo,OperatorWindow
from attendence.models import line1attendence,line2attendence,line3attendence,line4attendence,line5attendence
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
    today = str(date.today())
    if request.method=='POST' and 'linesubmit' in request.POST:
        lineno=request.POST['lineno']
        print('heklo')
        print(lineno)
        operator_list=UserProfileInfo.objects.filter(line_no=lineno)
        print(operator_list)
        return render(request,'authenticate/takeattendence.html',{'operator_list':operator_list,'line_no':lineno,'today':today})
    elif request.method=='POST' and 'attendencesubmit' in request.POST:
        a=submitattendence(request)
        print(a)
        if a==2:
            mess="Attendence submitted"
            return render(request,'authenticate/takeattendence.html',{'mess':mess,'today':today})
        elif a==1:
            mess="Already submitted"
            return render(request,'authenticate/takeattendence.html',{'mess':mess,'today':today})
        else:
            mess="Error Occured"
            return render(request,'authenticate/takeattendence.html',{'mess':mess,'today':today})

    return render(request,'authenticate/takeattendence.html',{'today':today})

def submitattendence(request):
    a=2
    lineno=request.POST['lineno']
    operators=UserProfileInfo.objects.filter(line_no=lineno)
    print('hello',lineno)
    if(int(lineno) == 1):
        print('true')
        attenddatescheck=line1attendence.objects.all()
        today = str(date.today())
        c=0
        for check in attenddatescheck:
            if(str(check.date)==today):
                c=1
        if(c==0):
            print('inside')
            for i in operators:
                attend=request.POST[i.operator_id]
                operatorAttend=line1attendence(operator_id=i.operator_id,operator_name=i.operator_name
                ,attendence=attend)
                operatorAttend.save()
                print(attend)
            return a
        else:
            a=1
            return a

    elif(int(lineno) == 2):
        print('true')
        attenddatescheck=line2attendence.objects.all()
        today = str(date.today())
        c=0
        for check in attenddatescheck:
            if(str(check.date)==today):
                c=1
        if(c==0):
            print('inside')
            for i in operators:
                attend=request.POST[i.operator_id]
                operatorAttend=line2attendence(operator_id=i.operator_id,operator_name=i.operator_name
                ,attendence=attend)
                operatorAttend.save()
                print(attend)
            return a
        else:
            a=1
            return a
    elif(int(lineno) == 3):
        print('true')
        attenddatescheck=line3attendence.objects.all()
        today = str(date.today())
        c=0
        for check in attenddatescheck:
            if(str(check.date)==today):
                c=1
        if(c==0):
            print('inside')
            for i in operators:
                attend=request.POST[i.operator_id]
                operatorAttend=line3attendence(operator_id=i.operator_id,operator_name=i.operator_name
                ,attendence=attend)
                operatorAttend.save()
                print(attend)
            return a
        else:
            a=1
            return a
    elif(int(lineno) == 4):
        print('true')
        attenddatescheck=line4attendence.objects.all()
        today = str(date.today())
        c=0
        for check in attenddatescheck:
            if(str(check.date)==today):
                c=1
        if(c==0):
            print('inside')
            for i in operators:
                attend=request.POST[i.operator_id]
                operatorAttend=line4attendence(operator_id=i.operator_id,operator_name=i.operator_name
                ,attendence=attend)
                operatorAttend.save()
                print(attend)
            return a
        else:
            a=1
            return a
    elif(int(lineno) == 5):
        print('true')
        attenddatescheck=line5attendence.objects.all()
        today = str(date.today())
        c=0
        for check in attenddatescheck:
            if(str(check.date)==today):
                c=1
        if(c==0):
            print('inside')
            for i in operators:
                attend=request.POST[i.operator_id]
                operatorAttend=line5attendence(operator_id=i.operator_id,operator_name=i.operator_name
                ,attendence=attend)
                operatorAttend.save()
                print(attend)
            return a
        else:
            a=1
            return a
def takeleave(request):
    return render(request,'authenticate/takeleave.html')

def leavesubmit(request):
    id=request.POST['operatorid']
    leavestart=request.POST['leavestart']
    leaveend=request.POST['leaveend']
    operators=line1attendence.objects.all()
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

def attendencereport(request):
    if request.method == 'POST':
        lineno=request.POST['lineno']
        if int(lineno)==1:
            reports=line1attendence.objects.all()
            return render(request,'authenticate/attendencereport.html',{'reports':reports})
        if int(lineno)==2:
            reports=line2attendence.objects.all()
            return render(request,'authenticate/attendencereport.html',{'reports':reports})
        if int(lineno)==3:
            reports=line3attendence.objects.all()
            return render(request,'authenticate/attendencereport.html',{'reports':reports})
        if int(lineno)==4:
            reports=line4attendence.objects.all()
            return render(request,'authenticate/attendencereport.html',{'reports':reports})
        if int(lineno)==5:
            reports=line5attendence.objects.all()
            return render(request,'authenticate/attendencereport.html',{'reports':reports})
    return render(request,'authenticate/attendencereport.html')
