"""FCS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from Users import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
	path('admin/', admin.site.urls),
	path('Wall/', include('Wall.urls')),
	path('register/',user_view.register,name="register"),
    path('profile/',user_view.profile,name="profile"),
    path('friends/',user_view.friend_page,name="friend_page"),
	path('login/', auth_view.LoginView.as_view(template_name='Users/login.html'), name='login'),
	path('logout/', auth_view.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('friends/add_friend/(?P<pk>\d+)/',user_view.add_friend,name="add_friend"),
    path('friends/remove_friend/(?P<pk>\d+)/',user_view.remove_friend,name="remove_friend"),
]
