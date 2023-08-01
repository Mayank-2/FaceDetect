from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from FaceR.camera import VideoCap
from django.http import HttpResponseRedirect
from FaceR.models import Org
from Account.forms import organization
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from FaceR.forms import Dash
from Account.models import HOD, Student
from FaceR.models import AttendanceCS, AttendanceCE, AttendanceME, AttendanceEC
from datetime import date, datetime, timedelta
# from django.contrib.auth import logout


Org_u = ''

def pre_home(request):
    return render(request,"app/pre_home.html")

def home(request):
    return render(request, 'app/home.html')


@login_required(login_url="/accounts/login/")
def record(request):
    # print(org)
    return render(request, 'app/record.html')


@login_required(login_url="/accounts/login/")
def dash(request):
    user = request.user
    if request.method == "POST":
        form = Dash(request.POST)
        if form.is_valid():
            branch = form.cleaned_data.get('Branch')
            Batch = form.cleaned_data.get('Batch')
            passwd = form.cleaned_data.get('passwd')
            try:
                org_u= Org.objects.get(user=user)
                HO_D = HOD.objects.get(branch=branch,org=org_u)
                if HO_D:
                    if HO_D.password == passwd:
                        # print(HO_D.branch)
                        if HO_D.branch == "CS" or HO_D.branch == "CSE":
                            student = Student.objects.filter(
                                org=org_u, branch=HO_D.branch, adm_year=Batch)
                            countStudent = 0
                            for i in student:
                                countStudent += 1

                            Attendance = AttendanceCS.objects.filter(org=org_u).filter(
                                adm_year=Batch).filter(Date=date.today())
                            countAttendance = 0
                            for i in Attendance:
                                countAttendance += 1
                            # last seven days data..........................................
                            last_Seven_ = datetime.today()-timedelta(days=7)
                            # today = date.today()
                            last_Seven_Attend = AttendanceCS.objects.filter(
                                Date__range=[last_Seven_, date.today()])

                            countlastseven = 0
                            for i in last_Seven_Attend:
                                countlastseven += 1
                            Averagelastseven = round(countlastseven / countStudent,2)
                            # last Month data ...............................................................
                            last_month_ = datetime.today()-timedelta(days=30)
                            last_month_Attend = AttendanceCS.objects.filter(
                                Date__range=[last_month_, date.today()])
                            countlastmonth = 0
                            for i in last_month_Attend:
                                countlastmonth += 1
                            Averagelastmonth = round(
                                countlastmonth / countStudent, 2)

                            return render(request, 'app/dash.html', {'Student': countStudent, 'Attendance': countAttendance, 'data': Attendance, 'lastseven': Averagelastseven, 'lastmonth': Averagelastmonth})
                        if HO_D.branch == "ME":
                            org_u = Org.objects.get(user=user)
                            student = Student.objects.filter(
                                org=org_u, branch=HO_D.branch, adm_year=Batch)
                            countStudent = 0
                            for i in student:
                                countStudent += 1

                            Attendance = AttendanceME.objects.filter(org=org_u).filter(
                                adm_year=Batch).filter(Date=date.today())
                            countAttendance = 0
                            for i in Attendance:
                                countAttendance += 1
                            # last seven days data..........................................
                            last_Seven_ = datetime.today()-timedelta(days=7)

                            last_Seven_Attend = AttendanceME.objects.filter(
                                Date__range=[last_Seven_, date.today()])

                            countlastseven = 0
                            for i in last_Seven_Attend:
                                countlastseven += 1
                            
                            Averagelastseven = round(countlastseven / countStudent, 2)
                            
                            # last Month data ...............................................................

                            last_month_ = datetime.today()-timedelta(days=30)
                            last_month_Attend = AttendanceME.objects.filter(
                                Date__range=[last_month_, date.today()])
                            countlastmonth = 0
                            for i in last_month_Attend:
                                countlastmonth += 1
                            Averagelastmonth = round(
                                countlastmonth / countStudent, 2)

                            return render(request, 'app/dash.html', {'Student': countStudent, 'Attendance': countAttendance, 'data': Attendance, 'lastseven': Averagelastseven, 'lastmonth': Averagelastmonth})

                        if HO_D.branch == "CE":
                            org_u = Org.objects.get(user=user)
                            student = Student.objects.filter(
                                org=org_u, branch=HO_D.branch, adm_year=Batch)
                            countStudent = 0
                            for i in student:
                                countStudent += 1

                            Attendance = AttendanceCE.objects.filter(org=org_u).filter(
                                adm_year=Batch).filter(Date=date.today())
                            countAttendance = 0
                            for i in Attendance:
                                countAttendance += 1
                            # last seven days data..........................................
                            last_Seven_ = datetime.today()-timedelta(days=7)
                            # today = date.today()
                            last_Seven_Attend = AttendanceCE.objects.filter(
                                Date__range=[last_Seven_, date.today()])

                            countlastseven = 0
                            for i in last_Seven_Attend:
                                countlastseven += 1
                            Averagelastseven = round(countlastseven / countStudent,2)

                            # last Month data ...............................................................
                            last_month_ = datetime.today()-timedelta(days=30)
                            last_month_Attend = AttendanceCE.objects.filter(
                                Date__range=[last_month_, date.today()])
                            countlastmonth = 0
                            for i in last_month_Attend:
                                countlastmonth += 1
                            Averagelastmonth = round(
                                countlastmonth / countStudent, 2)

                            return render(request, 'app/dash.html', {'Student': countStudent, 'Attendance': countAttendance, 'data': Attendance, 'lastseven': Averagelastseven, 'lastmonth': Averagelastmonth})
                        if HO_D.branch == "EC":
                            org_u = Org.objects.get(user=user)
                            student = Student.objects.filter(
                                org=org_u, branch=HO_D.branch, adm_year=Batch)
                            countStudent = 0
                            for i in student:
                                countStudent += 1

                            Attendance = AttendanceEC.objects.filter(org=org_u).filter(
                                adm_year=Batch).filter(Date=date.today())
                            countAttendance = 0
                            for i in Attendance:
                                countAttendance += 1
                            # last seven days data..........................................
                            last_Seven_ = datetime.today()-timedelta(days=7)
                            # today = date.today()
                            last_Seven_Attend = AttendanceEC.objects.filter(
                                Date__range=[last_Seven_, date.today()])

                            countlastseven = 0
                            for i in last_Seven_Attend:
                                countlastseven += 1
                            Averagelastseven = round(countlastseven / countStudent,2)
                            # last Month data ...............................................................
                            last_month_ = datetime.today()-timedelta(days=30)
                            last_month_Attend = AttendanceEC.objects.filter(
                                Date__range=[last_month_, date.today()])
                            countlastmonth = 0
                            for i in last_month_Attend:
                                countlastmonth += 1
                            Averagelastmonth = round(
                                countlastmonth / countStudent, 2)

                            return render(request, 'app/dash.html', {'Student': countStudent, 'Attendance': countAttendance, 'data': Attendance, 'lastseven': Averagelastseven, 'lastmonth': Averagelastmonth})
                    else:
                        return render(request,'error/HOD_error.html',{'error':'HOD password is incorrect.'})
            except:
                return render(request,'error/error.html')     
    else:
        form = Dash()
    return render(request, 'form/dashform.html', {'form': form})


@login_required(login_url="/accounts/login/")
def org(request):
    user = request.user
    if request.method == "POST":
        form = organization(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data.get('name')
            contact = form.cleaned_data.get('contact')
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            postalcode = form.cleaned_data.get('postalcode')
            email = form.cleaned_data.get('email')
            userr = request.user
            data = Org(user=userr, name=name, contact=contact, address=address,
                       city=city, state=state, postalcode=postalcode, email=email)
            data.save()
            messages.success(request, "submission successful")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        data = Org.objects.filter(user=user)
        form = organization()
        return render(request, 'app/orgDetail.html', {'data': data, "form": form})

@login_required(login_url="/accounts/login/")
def index(request):
    return render(request, 'app/main.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@login_required(login_url="/accounts/login/")
def video_feed(request):
    user = request.user
    global org_u
    org_u = Org.objects.get(user=user)
    return StreamingHttpResponse(gen(VideoCap()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
 

def window_error(request):
    return render(request,'error/window_error.html')