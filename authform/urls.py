from django.conf.urls import url
from . import views

app_name = 'authform'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^success/$', views.success, name="success"),
    url(r'^fail/$', views.fail, name="fail"),
    url(r'^api/signin/$', views.signin_api, name="signin_api"),
    url(r'^api/signup/$', views.signup_api, name="signup_api"),
]
