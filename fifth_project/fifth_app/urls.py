from django.conf.urls import url
from fifth_app import views

app_name = 'other_links'

urlpatterns = [
  url(r'^registration/',views.register,name='register'),
  url(r'^login/',views.user_login,name='user_login')
  #url(r'^login/',views.login,name='login'),
]
