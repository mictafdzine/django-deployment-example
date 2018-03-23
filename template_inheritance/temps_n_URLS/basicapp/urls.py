from django.conf.urls import url
#from django.contrib import admin
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
url(r'^Other/$',views.Other, name = 'other'),
url(r'^relative_url_templates/$',views.relative_url_templates, name = 'relative_url_templates'),
 ]
