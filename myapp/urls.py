from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('back/',views.back,name='back'),
    path('change_password/',views.change_password,name='change_password'),
    path('new_password/',views.new_password,name='new_password'),
    path('photo_capture/',views.photo_capture,name='photo_capture'),
    path('visitor_view/',views.visitor_view,name='visitor_view'),
    path('visitor_exit/',views.visitor_exit,name='visitor_exit'),
    
]