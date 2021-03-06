"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from todo import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.index_register, name='register'),
    url(r'^login/', views.index_login, name='login'),

    url(r'^user_page/', views.user_page, name='user_page'),
    url(r'^user_update/', views.user_update, name='user_update'),
    url(r'^$', views.index, name='index'),
    url(r'^add/', views.add_todo, name='add_todo'),
    url(r'^detail_todo/(?P<todo_id>\d+)/', views.detail_todo, name='detail_todo'),
    url(r'^do/(?P<id>\d+)/', views.do_todo, name='do_todo'),
    url(r'^del/(?P<id>\d+)/', views.del_todo),
]
