import logging
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import time

logger = logging.getLogger('app')
config = settings.CONFIG


class LiveStatus(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LiveStatus, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'twitch/live-status.html')

    def post(self, request):
        channel = request.POST['twitch-channel']
        logger.info(channel)

        time.sleep(3)

        if channel == 'fail':
            data = {'success': False, 'channel': channel}
            return JsonResponse(data, status=400)
        else:
            data = {'success': True, 'channel': channel}
            return JsonResponse(data)
