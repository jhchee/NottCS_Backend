from django.conf.urls import url, include
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'event', EventViewSet, base_name='event')

urlpatterns = {
    url(r'^member/$', MemberCreateView.as_view(), name="create"),
    url(r'^member/(?P<pk>[0-9]+)/$',MemberDetailsView.as_view(), name="details"),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls