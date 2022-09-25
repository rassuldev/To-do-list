from urllib import request
from django.shortcuts import render
from .models import ToDoListItem
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo')

    # After registration go to main page
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class MyListView(LoginRequiredMixin, ListView):
    model = ToDoListItem
    context_object_name = 'tasks'
    template_name = 'todolist.html'

    # Get User specific data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


class CreateTask(CreateView):
    model = ToDoListItem
    fields = '__all__'
    success_url = reverse_lazy('todo')

    # Get User Specific Data
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


def addTodoView(request):
    x = request.POST['content']
    if len(x) != 0:
        new_item = ToDoListItem(content=x)
        new_item.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def deleteTodoView(request, i):
    y = ToDoListItem.objects.get(id=i)
    y.completed = True
    y.save()
    return HttpResponseRedirect('/todolistapp/')
