from django.contrib import admin
from django.urls import path, include
from hms import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('hospital/', include('hms.urls')),

]
