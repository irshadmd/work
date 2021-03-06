from django.shortcuts import render
from authenticate.forms import UserForm,windowForm
from .models import UserProfileInfo,OperatorWindow
from attendence.models import line1attendence,line2attendence,line3attendence,line4attendence,line5attendence
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from datetime import date

def index(request):
    return render(request,'authenticate/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")

def logout(request):
    return HttpResponseRedirect(reverse('index'))
def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            print('true')
            operator_id=request.POST['operator_id']
            password=request.POST['password']
            operators=UserProfileInfo.objects.all()
            print(operator_id)
            c=0
            for i in operators:
                if(i.operator_id==operator_id):
                    c=1
            if(c==1):
                mess="UserId is Already used"
                user_form = UserForm()
                return render(request,'authenticate/registration.html',
                                      {'user_form':user_form,'mess':mess})
            else:
                add_user(request)
                return render(request,'authenticate/login.html')
    else:
        user_form = UserForm()
        return render(request,'authenticate/registration.html',
                            {'user_form':user_form})
def add_user(request):
	operator_name=request.POST['operator_name']
	operator_id=request.POST['operator_id']
	line_no=request.POST['line_no']
	address=request.POST['address']
	product_category=request.POST['product_category']
	product_sub_category=request.POST['product_sub_category']
	operation=request.POST['operation']
	operation_complexity=request.POST['operation_complexity']
	no_of_operation=request.POST['no_of_operation']
	skill_percentage=request.POST['skill_percentage']
	grade=request.POST['grade']
	password=request.POST['password']

	user_info=UserProfileInfo(operator_name=operator_name,operator_id=operator_id,line_no=line_no,address=address,product_category=product_category
		,product_sub_category=product_sub_category,operation=operation,operation_complexity=operation_complexity
		,no_of_operation=no_of_operation,skill_percentage=skill_percentage,grade=grade,password=password)
	user_info.save()


def user_login(request):
    if request.method == 'POST':
        operator_id = request.POST.get('operator_id')
        password = request.POST.get('password')
        result=UserProfileInfo.objects.filter(operator_id=operator_id,password=password)
        if result:
            for i in result:
                name=i.operator_name
                id=i.operator_id
                product=i.product_category
            hr = str(datetime.datetime.now().hour)
            min = str(datetime.datetime.now().minute)
            time=hr+':'+min
            year = str(datetime.datetime.now().year)
            month = str(datetime.datetime.now().month)
            day = str(datetime.datetime.now().day)
            date=day+'/'+month+'/'+year
            print(name,id,product,time,date)
            return render(request, 'authenticate/operator_window.html', {'name':name,'id':id,'product':product,'time':time,'date':date})
        else:
            register='You have to register than you can login'
            return render(request, 'authenticate/login.html', {'registerfirst':register})
    else:
        return render(request, 'authenticate/login.html', {})

def window(request):
    if request.method =='POST':
        form=windowForm(request.POST)
        if form.is_valid():
            print('Window Form')

    form=windowForm()
    return render(request,'authenticate/operator_window.html',{'form':form})

def windowsubmit(request):
    operator_id =request.POST['opid']
    operator_name =request.POST['opname']
    operation=request.POST['operation']
    start_time=request.POST['optime']
    hr = str(datetime.datetime.now().hour)
    min = str(datetime.datetime.now().minute)
    time=hr+':'+min
    stop_time=time
    duration=time
    date=request.POST['opdate']
    machine_stop_time=time
    machine_run_time=request.POST['optime']
    machine_breakdown_time=time
    frequency_of_machine_stop=0
    ticket_no_start=request.POST['ticketnostart']
    ticket_no_end=request.POST['ticketnoend']
    total_pieces=1
    ticket_no_run_time=0
    next_ticket_no_time=0
    ct='test'
    total_stitched_pieces=request.POST['stitchedpieces']
    rework_ticket_no=request.POST['reworkticketno']
    rework_pieces=request.POST['reworkpieces']

    window_info=OperatorWindow(operator_id=operator_id,operator_name=operator_name,operation=operation,start_time=start_time
		,stop_time=stop_time,duration=duration,date=date,machine_stop_time=machine_stop_time,machine_run_time=machine_run_time
        ,machine_breakdown_time=machine_breakdown_time,frequency_of_machine_stop=frequency_of_machine_stop
        ,ticket_no_start=ticket_no_start,ticket_no_end=ticket_no_end,total_pieces=total_pieces,ticket_no_run_time=ticket_no_run_time
        ,next_ticket_no_time=next_ticket_no_time,ct=ct,total_stitched_pieces=total_stitched_pieces,rework_ticket_no=rework_ticket_no
        ,rework_pieces=rework_pieces)
    window_info.save()
    return render(request,'authenticate/index.html')

def operatorskillmatrix(request):
    operator_list=UserProfileInfo.objects.all()
    operator_attendences=line1attendence.objects.all()
    cdate=str(date.today())
    return render(request,'authenticate/operator_skill_matrix.html',{'operator_list':operator_list
    ,'operator_attendences':operator_attendences,'cdate':cdate})
