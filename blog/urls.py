from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'moments_input', views.moments_input),
    url(r'', views.welcome),
]