
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountApp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld() #모델 객체 생성
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountApp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountApp/hello_world.html', context={'hello_world_list': hello_world_list})

