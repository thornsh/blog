"""for users'model"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # login in window
    url(r'^login/$',login,{'template_name':'users/login.html'},
    	name = 'login'),

    # logout
    url(r'^logout/$',views.logout_view,name = 'logout'),

    # register
    url(r'^register/$',views.register,name = 'register'),
]