from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    elif request.method == "GET":
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'