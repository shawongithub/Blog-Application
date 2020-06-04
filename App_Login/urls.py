
from django.urls import path
from App_Login import views
app_name='App_Login'

urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_profile/',views.change_profile,name='change_profile'),
    path('password/',views.change_password,name='password'),
    path('add_picture/',views.add_pro_pic,name='add_picture'),
    path('change_picture/',views.change_picture, name='change_picture'),
]