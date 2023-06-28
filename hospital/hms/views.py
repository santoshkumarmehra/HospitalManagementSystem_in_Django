from django.shortcuts import render, redirect
from .forms import  LoginForm, DoctorSignUpForm, PatientSignUpForm
from django.views.generic.base import TemplateView 
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from .models import *


class Home(TemplateView):
    template_name = 'hms/home.html/'


class DoctorRegistration(View):
    def get(self, request):
        doctor_form = DoctorSignUpForm()
        return render(request, 'hms/doctor_registration.html', {'doctor_form':doctor_form})
    
    def post(self, request):
        doctor_form = DoctorSignUpForm(request.POST)
        if doctor_form.is_valid():
            data = doctor_form.save(commit=False)
            data.password = make_password(data.password)
            data.save()
            return redirect('doctor-registration')


class PatientRegistration(View):
    def get(self, request):
        patient_form = PatientSignUpForm()
        return render(request, 'hms/patient_registration.html', {'patient_form':patient_form})
    
    def post(self, request):
        patient_form = PatientSignUpForm(request.POST)
        if patient_form.is_valid():
            data = patient_form.save(commit=False)
            data.password = make_password(data.password)
            data.save()
            return redirect('doctor-registration')



class DesignationView(View):
    def get(self, request):
        designation = request.GET.get('designation')
        if designation=='doctor':
            return redirect('doctor-registration')
        elif designation=='patient':
            return redirect('patient-registration')
        else:
            return render(request, 'hms/designation.html')


class Login(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'hms/login.html/', {'login_form': login_form})
    
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            encryptedpassword=make_password(password)
            checkpassword=check_password(password, encryptedpassword)
            if checkpassword==False:
                return redirect('login')
            try:
                user_data = UserProfile.objects.get(email=email)
                user_category = user_data.category.name
                if user_data.category.name=='Patient':
                    request.session['variable'] = user_category
                    return redirect('hospital_main_page')
                if user_data.category.name=='Doctor':
                    request.session['variable'] = user_category
                    return redirect('hospital_main_page')            
            except UserProfile.DoesNotExist:
                return redirect('login')
        else:
            return redirect('login')


class Logout(LogoutView):
    template_name = 'hms/logout.html/'


class HospitalView(View):
    def get(self, request):
        user_category = request.session['variable']
        user_category_data = UserProfile.objects.filter(category__name=user_category).first()
        print(user_category_data.first_name)
        print(user_category_data.category.name)
        if user_category=='Patient':
            return render(request, 'hms/hospital_main_page.html/', { 'user_category_data': user_category_data})
    

