from django.urls import re_path

from . import views

app_name = 'accounts'

urlpatterns = [
    re_path('logout/$', views.LogoutView.as_view(), name="logout"),
    re_path('signup/$', views.SignUpView.as_view(), name="signup"),
]
