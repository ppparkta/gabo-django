from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()
        return HttpResponseRedirect('/account/hello_world')

    elif request.method == "GET":
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
