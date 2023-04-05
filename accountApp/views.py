from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# 함수과 클래스가 불러와지는 방식이 달라서 함수에서는 reverse / 클래스에서는 reverse_lazy 사용
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountApp.forms import AccountUpdateForm
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

#------------------------------------------------------------------------------------------------------------

class AccountCreateView(CreateView):
    model = User # 장고에서 기본 제공하는 모델 사용
    form_class = UserCreationForm # 기본 제공하는 계정 폼
    success_url = reverse_lazy('accountApp:hello_world') # 계정 생성에 성공했다면 어떤 url로 이동할 것인가
    template_name = 'accountapp/create.html' # 회원가입할 때의 template 경로 지정

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountApp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountApp:login')
    template_name = 'accountapp/delete.html'