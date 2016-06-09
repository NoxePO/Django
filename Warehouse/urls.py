"""Warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Product import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^login/$', auth_views.login, {'template_name' : 'login.html'}, name = 'login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : 'home'}, name = 'logout'),
	
	url(r'^pdf/', views.generatepdf, name = 'generatepdf'),
	
	url(r'^prod_new/', views.prod_new),
    url(r'^prod_edit/(?P<cpk>\d+)$', views.prod_edit, name='prod_edit'),
    url(r'^prod_del/(?P<cpk>\d+)$', views.prod_delete, name='prod_del'),
	
	url(r'^order_new/', views.order_new),
    url(r'^order_edit/(?P<cpk>\d+)$', views.order_edit, name='order_edit'),
    url(r'^order_del/(?P<cpk>\d+)$', views.order_delete, name='order_del'),
	
	url(r'^worker_new/', views.worker_new),
    url(r'^worker_edit/(?P<cpk>\d+)$', views.worker_edit, name='worker_edit'),
    url(r'^worker_del/(?P<cpk>\d+)$', views.worker_delete, name='worker_del'),
	
	
	
    url(r'', views.home, name='home'),
]
