"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

import hello.views
import worddb.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', hello.views.hello),
    url(r'^hello/(?P<name>\w+)/', hello.views.named),

    url(r'^path/', hello.views.path),
    url(r'^query/', hello.views.query),
    url(r'^method/', hello.views.method),
    url(r'^headers/', hello.views.headers),

    url(r'^index/', hello.views.index),

    url(r'^about/', hello.views.about),
    url(r'^support/', hello.views.support),

    url(r'^session/', hello.views.session),

    url(r'^words/', worddb.views.words),
    url(r'^word/(?P<word>\w+)', worddb.views.detail),

]
