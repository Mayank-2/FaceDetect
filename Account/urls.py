from django.urls import path,include
from Account import views
from django.contrib.auth import views as auth_views
from Account.forms import Log_in 
from django.conf.urls.static import static  
from django.conf import settings
# from Account.views import add_to_cart_,cart

urlpatterns = [

    path('signup/',views.CustomerRegistration.as_view(),name='signup'),

    path('logout/',auth_views.LogoutView.as_view(),name='logout'), 

    path('hod/',views.H_O_D,name='hod'),

    path('HodLogin/',views.H_O_DLogin,name="HODLogin"),

    path('HODMain/',views.HO_DMain,name="HODMain"),

    path("addStu/",views.add_stud,name='addstu'),

    path('DeleteStud/',views.delete_Stud,name="DeleteStud"),

    path('HOD_Attend/',views.HOD_showAttend,name="HOD_showAttend"),

    path("StuDrop/",views.stuDropDown,name='StudDrop'),

    path("showAttend/",views.showAttend,name="showAttend")



]