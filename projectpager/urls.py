from django.conf.urls import url
from . import views

urlpatterns = [
  url(
    r'^new/$',
    views.ProjectPageCreateView.as_view(),
    name='projectpage_create'
  ),
  url(
    r'^list/$',
    views.ProjectPageListView.as_view(),
    name='projectpage_list'
  ),
  url(
    r'^(?P<pk>\w+)/detail/$',
    views.ProjectPageDetailView.as_view(),
    name='project_page_detail'
  ),
]