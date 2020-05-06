from django.urls import path,include,re_path
from thirdapp.views import SchoolListView,SchoolDetailView
app_name='basic_app'
urlpatterns=[
    path('first',SchoolListView.as_view(),name='list'), #CLASS BASED VIEW URL PATTERNS
    re_path(r'^(?P<pk>[-\w]+)/$',SchoolDetailView.as_view(),name='detail'),
 ]
