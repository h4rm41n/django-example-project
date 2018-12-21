from django.contrib import admin
from django.urls import path, include
from surat_menyurat import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('home/', views.home, name='home'),    
    path('surat/', include('surat_menyurat.urls', namespace="surat")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
