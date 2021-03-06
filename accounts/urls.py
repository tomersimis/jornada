"""jornada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^cadastro-professor$', 'accounts.views.signup_teacher', name = 'signup_teacher'),
    url(r'^cadastro-aluno$', 'accounts.views.signup_student', name = 'signup_student'),
    url(r'^login/', 'accounts.views.login', name = "login"),
    url(r'^editar/', 'accounts.views.edit', name = "edit"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name= 'logout'),
    url(r'^perfil-aluno/(?P<id>\d+)/$', 'accounts.views.view_student', name='view'),
    url(r'^perfil-professor/(?P<id>\d+)/$', 'accounts.views.view_teacher', name='viewteacher')
]
