from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('predict/',views.predict_view,name='predict'),
    path('user_signup/',views.user_register,name='user_register'),
    path('doctor_signup/',views.doctor_register,name='doctor_register'),
    path('doctor_login/',views.doctor_login,name='doctor_login'),
    path('doctor_feedback/',views.feedback,name='feedback'),
    path('index/',views.apredict,name='apredict'),
    path('logout/',views.logout_view,name='logout'),
    path('last_patients/',views.doctor_patient_details_view_last,name='doctor_patient_details_last'),
    path('all_patients/',views.doctor_patient_details_view_all,name='doctor_patient_details_all'),
]
