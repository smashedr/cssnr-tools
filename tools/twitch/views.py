import logging
from django.conf import settings
from django.shortcuts import render

logger = logging.getLogger('app')
config = settings.CONFIG


def live_status(request):
    # View: /twitch/live-status/
    return render(request, 'twitch/live-status.html')
