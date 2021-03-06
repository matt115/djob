"""social_network URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import CustomLoginView
# https://docs.djangoproject.com/en/1.11/ref/views/#django.views.static.serve

urlpatterns = [
    url(r'^$', CustomLoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^inbox/notification', include('notifications.urls', namespace='notifications')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^friendship/', include('friendship.urls', namespace='friendship')),
    url(r'^messanger/', include('messanger.urls', namespace='messanger')),
    url(r'^pages/', include('projectpager.urls', namespace='projectpager')),
    url(r'^search/', include('searcher.urls', namespace='searcher')),
    url(r'^', include('authentication.urls', namespace='authentication')),
    url(r'^skill/', include('skiller.urls', namespace='skill')),
    url(r'^notifications/', include('marathon.urls', namespace='marathon')),
    url(r'^recommander/', include('recommander.urls', namespace='recommander')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
