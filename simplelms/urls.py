"""simplelms URL Configuration

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
#([0-9]+)

from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from simplelms.core.views import index,category,book
from simplelms.core import views
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/(?P<category_id>\d+)$',category,name="category"),
    url(r'^book/(?P<book_id>\d+)$',book,name="book"),
    url(r'^$',index,name="index"),
    url(r'^', include(router.urls)),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
