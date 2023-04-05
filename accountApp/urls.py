from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountApp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountApp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 기본 제공하는 user를 사용하여 views.py에 클래스 작성하지 않고 url에서 바로 지정 후 템플릿 연결

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accountapp/logout.html'), name='logout'),

    # view단에 함수형 뷰는 그냥 함수명만 적으면 되지만 class base 뷰는 클래스명과 .as_view() 메서드를 적어주어야한다.
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]
