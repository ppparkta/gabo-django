from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accountapp:login'))
    else:
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

class AccountDetailView(DeleteView):
    model = User
    context_object_name = 'target_user' #템플릿에서 사용하는 user객체의 이름을 다르게 설정할 수 있음
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()