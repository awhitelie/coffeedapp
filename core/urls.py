from django.conf.urls import patterns, include, url
from django.conf.urls import include, url
import core.views as coreviews

urlpatterns = [
    url(r'^$', coreviews.LandingView.as_view()),
    url(r'location/$', coreviews.LocationListView.as_view()),
]
