from django.urls import path

import tools.twitch.views as view

urlpatterns = [
    path('live-status/', view.LiveStatus.as_view(), name='twitch.live_status'),
    path('agdq-streamers/', view.AgdqStreamers.as_view(), name='twitch.agdq_streamers'),
]
