"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from NewsApp1 import views as views1
from registrationLogin import views as views2
from Posts import views as views3

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views1.home, name='home'),
    path('register/', views2.register, name='register'),
    path('update/', views2.Update, name='update'),
    path('accounts/profile/', login_required(views1.profile), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='NewsApp1/login.html'), name='login'),  # Logging in
    path('logout/', auth_views.LogoutView.as_view(template_name='NewsApp1/logout.html'), name='logout'),  # Logging out
    path('about_us/', views1.about_us, name='about us')
]
