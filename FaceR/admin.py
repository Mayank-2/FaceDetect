from django.contrib import admin
from FaceR.models import Org,AttendanceCS,AttendanceCE,AttendanceME,AttendanceEC

# Register your models here.
admin.site.register(Org)


admin.site.register(AttendanceCS)
admin.site.register(AttendanceCE)
admin.site.register(AttendanceME)
admin.site.register(AttendanceEC)