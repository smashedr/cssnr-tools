from django.urls import path

import tools.twitch.views as view

urlpatterns = [
    path('live-status', view.live_status, name='twitch.live_status'),
]
