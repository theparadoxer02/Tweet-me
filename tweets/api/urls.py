from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
	RetweetAPIView,
    TweetCreateAPIView,
    TweetListAPIView,
    LikeToggleAPIView,
    )

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), 
    url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'), # /tweet/1/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]

