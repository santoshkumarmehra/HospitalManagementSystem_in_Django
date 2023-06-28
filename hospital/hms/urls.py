from django.urls import path
from . import views


urlpatterns = [
    path('designation_url/', views.DesignationView.as_view(), name='designation_url'),
    path('doctor-registration/', views.DoctorRegistration.as_view(), name='doctor-registration'),
    path('patient-registration/', views.PatientRegistration.as_view(), name='patient-registration'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('hospital_main_page/', views.HospitalView.as_view(), name='hospital_main_page'),

]