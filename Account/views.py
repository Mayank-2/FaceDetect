from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Sign_up
from django.views import View
from django.contrib import messages
from Account.forms import Studentdata, organization, showStu, FindAttend, HodForm ,HodLogin , DeleteStud ,HODdAttend
from Account.models import Student, HOD , TempBranch
from django.contrib.auth.models import User
from FaceR.models import Org
from django.contrib.auth.decorators import login_required
from FaceR.models import AttendanceCS, AttendanceCE, AttendanceME, AttendanceEC
from django.contrib.auth.forms import AuthenticationForm
from datetime import date
import os

class CustomerRegistration(View):
    def get(self, request):
        form = Sign_up()
        return render(request, 'Account/signup.html', {'form': form})

    def post(self, request):
        form = Sign_up(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Signup Successfull! Please Login")
            return HttpResponseRedirect('/accounts/login/')
        return render(request, 'Account/signup.html', {'form': form})
    
@login_required(login_url="/accounts/login/")
def H_O_D(request):
    if request.method == "POST":
        form = HodForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data.get('name')
            branch = form.cleaned_data.get('branch')
            passwd = form.cleaned_data.get('passwd')
            passwdd_ = form.cleaned_data.get('passwdD_')
            try:
                org_u = Org.objects.get(user=user)
                print(org_u)
                data = HOD(org=org_u,name=name,branch=branch,password=passwd)
                data.save()
                messages.success(request, "submission successful")
                return HttpResponseRedirect("/acc/HodLogin/")
            except:
                return render(request,"error/error.html",{'error':'this name of HOD is already exist somewhere.'})
        return render(request, 'form/hod.html', {'form': form})
    else:
        form = HodForm()
            # img = Studentdata.objects.all()
        return render(request,'form/hod.html', { "form": form})
    
@login_required(login_url="/accounts/login/")
def H_O_DLogin(request):
    if request.method == "POST":
        form = HodLogin(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data.get('name')
            branch = form.cleaned_data.get('branch')
            passwdd_ = form.cleaned_data.get('password')
            
            try:
               org_u= Org.objects.get(user=user)
               HO_D= HOD.objects.get(name=name,branch=branch,org=org_u)
               
               if HO_D:
                   if HO_D.branch==branch:
                        if HO_D.password == passwdd_:
                                record = TempBranch.objects.get(id=1)
                                record.branch = HO_D.branch
                                record.save()
                                return HttpResponseRedirect("/acc/HODMain/")

                        else:
                            messages.warning(request,"Password is incorrect.")
                   else:
                       messages.warning(request,"Branch is incorrect.")
            except:
               messages.warning(request, 'Error, either Email or Password is not correct.')
        return render(request, 'form/HODLogin.html', {'form': form})
    else:
        form = HodLogin()
        return render(request, 'form/HODLogin.html', {'form': form})
    
@login_required(login_url="/accounts/login/")
def HO_DMain(request):
    return render(request, 'app/HODMain.html')

@login_required(login_url="/accounts/login/")
def HOD_showAttend(request): 
    if request.method == "POST":
        form = HODdAttend(request.POST)
        if form.is_valid():
            Temp_branch = TempBranch.objects.get(id=1)
            Branch = Temp_branch.branch
            Date = date.today()
            Batch = form.cleaned_data.get('Batch')
            user = request.user
            org_u= Org.objects.get(user=user)
            if Branch == "CS" or Branch=="CSE":
                student = AttendanceCS.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                return render(request, 'Attendance/HODAttend.html', {"showAttend":student})
            if Branch == "ME":
                student = AttendanceME.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                return render(request, 'Attendance/HODAttend.html', {"showAttend":student})
            if Branch == "CE":
                student = AttendanceCE.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                return render(request, 'Attendance/HODAttend.html', {"showAttend":student})
            if Branch == "EC":
                student = AttendanceEC.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                return render(request, 'Attendance/HODAttend.html', {"showAttend":student})
    else:
        form = HODdAttend()
        return render(request, 'form/HODFindAttend.html', {"FindStud": form})


@login_required(login_url="/accounts/login/")
def add_stud(request):
    if request.method == "POST":
        form = Studentdata(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data.get('name')
            enroll = form.cleaned_data.get('enrollment')
            Temp_branch = TempBranch.objects.get(id=1)
            branch = Temp_branch.branch
            ad_year = form.cleaned_data.get('adm_year')
            image = form.cleaned_data.get('image')
            try:
                org_u = Org.objects.get(user=user)
                data = Student(org=org_u,name=name,enrollment=enroll,branch=branch,adm_year=ad_year,image=image)
                data.save()
                messages.success(request, "submission successful" )
                return HttpResponseRedirect("/acc/HODMain/")
            except:
                return render(request,"error/error.html",{'error':'A student already exists for this enrollment number.'})
            
        return render(request, 'form/addstu.html', {'form': form})
    else:
        form = Studentdata()
        user = request.user
        global org 
        org = Org.objects.get(user=user)
        # img = Studentdata.objects.all()
        return render(request, 'form/addstu.html', { "form": form})
    
@login_required(login_url="/accounts/login/")
def delete_Stud(request):
    if request.method == "POST":
        form = DeleteStud(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data.get('name')
            enroll = form.cleaned_data.get('enrollment')
            Temp_branch = TempBranch.objects.get(id=1)
            branch = Temp_branch.branch
            ad_year = form.cleaned_data.get('adm_year')
            try:
                org_u = Org.objects.get(user=user)
                data = Student.objects.filter(org=org_u,name=name,enrollment=enroll,branch=branch,adm_year=ad_year)
                if data:
                    data.delete()
                else:
                    return render(request,"error/error.html",{'error':'There is no student for this credential.'})
            except:
                return render(request,"error/error.html")
            return HttpResponseRedirect("/acc/HODMain/")
        return render(request, 'form/deleteStud.html', {'form': form})
    else:
        form = DeleteStud()
        # img = Studentdata.objects.all()
        return render(request, 'form/deleteStud.html', { "form": form})

@login_required(login_url="/accounts/login/")
def stuDropDown(request):
    print("hello")
    if request.method == "POST":
        form = showStu(request.POST)
        if form.is_valid():
            user = request.user
            Branch = form.cleaned_data.get('Branch')
            Batch = form.cleaned_data.get('Batch')
            print(Branch)
            try:
                org_u = Org.objects.get(user=user)
                student = Student.objects.filter(branch=Branch).filter(adm_year=Batch).filter(org=org_u)

                return render(request, 'form/showStudentdata.html', {"students":student})
            except:
                return render(request,"error/error.html")
    else:
        form = showStu()
        return render(request, 'form/showstudent.html', {"stuform": form})
    
@login_required(login_url="/accounts/login/")
def showAttend(request):
    if request.method == "POST":
        form = FindAttend(request.POST)
        if form.is_valid():
            Branch = form.cleaned_data.get('Branch')
            Date = form.cleaned_data.get('Date')
            Batch = form.cleaned_data.get('Batch')
            user = request.user
            try:
                org_u= Org.objects.get(user=user)
                if Branch == "CS" or Branch=="CSE":
                    student = AttendanceCS.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                    return render(request, 'Attendance/showAttend.html', {"showAttend":student})
                if Branch == "ME":
                    student = AttendanceME.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                    return render(request, 'Attendance/showAttend.html', {"showAttend":student})
                if Branch == "CE":
                    student = AttendanceCE.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                    return render(request, 'Attendance/showAttend.html', {"showAttend":student})
                if Branch == "EC":
                    student = AttendanceEC.objects.filter(org=org_u).filter(adm_year=Batch).filter(Date=Date)
                    return render(request, 'Attendance/showAttend.html', {"showAttend":student})
            except:
                return render(request,"error/error.html")
    else:
        form = FindAttend()
        return render(request, 'form/FindStud.html', {"FindStud": form})

 