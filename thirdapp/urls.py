from django.urls import path,include,re_path
from thirdapp.views import SchoolListView,SchoolDetailView,SchoolCreateView,SchoolUpdateView,SchoolRemoveView
app_name='basic_app'
urlpatterns=[
    path('first',SchoolListView.as_view(),name='list'), #CLASS BASED VIEW URL PATTERNS
    re_path(r'^(?P<pk>\d+)/$',SchoolDetailView.as_view(),name='detail'),
    path('create/',SchoolCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$',SchoolUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$',SchoolRemoveView.as_view(),name='delete'),

 ]
