"""todolistproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from todolistapp.views import addTodoView, deleteTodoView, CustomLoginView, MyListView, CreateTask, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('todolistapp/', MyListView.as_view(), name='todo-list'),
    path('addTodoItem/', CreateTask.as_view(), name='task-create'),
    path('deleteTodoItem/<int:i>/', deleteTodoView, name='task-delete'),
    path('', MyListView.as_view(), name='todo'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
