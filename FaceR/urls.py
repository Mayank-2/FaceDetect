from django.urls import path,include
from FaceR import views
from Account.forms import Log_in
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('',views.pre_home),
    path('cam/',views.video_feed,name='video_feed'),
    path('home/',views.home),
    path('acc/',include('Account.urls')),
    path('camOn/',views.index,name="cam"),
    path('rec/',views.record,name='record'),
    path('dash/',views.dash,name='dash'),
    path('Org/',views.org,name='OrDetail'),
    ##########################################
    path('accounts/login/',auth_views.LoginView.as_view(template_name = 'Account/login.html', authentication_form =Log_in),name='login'),

    path('window_error/',views.window_error)

    
]