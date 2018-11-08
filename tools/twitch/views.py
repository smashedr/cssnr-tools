import logging
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from tools.twitch.functions import this_is_more_than_a_function, agdq

logger = logging.getLogger('app')
config = settings.CONFIG


class LiveStatus(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LiveStatus, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'twitch/live-status.html')

    def post(self, request):
        try:
            channel = request.POST['twitch-channel']
            chatters = True if 'process-chatters' in request.POST else False
            logger.info(chatters)
            logger.info(channel)
            results = this_is_more_than_a_function(channel, chatters=chatters)
            # results = {'success': False, 'data': 'ohhi'}
            logger.info('results: %s', results['data'])
            if results['success']:
                data = {'success': True, 'results': results['data']}
                return JsonResponse(data)
            else:
                data = {'success': False, 'results': results['data']}
                return JsonResponse(data, status=400)
        except Exception as error:
            logger.exception(error)
            data = {'success': False, 'error': error}
            return JsonResponse(data, status=500)


class AgdqStreamers(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AgdqStreamers, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'twitch/agdq-streamers.html')

    def post(self, request):
        try:
            results = agdq()
            logger.info('results: %s', results['data'])
            if results['success']:
                data = {'success': True, 'results': results['data']}
                return JsonResponse(data)
            else:
                data = {'success': False, 'results': results['data']}
                return JsonResponse(data, status=400)
        except Exception as error:
            logger.exception(error)
            data = {'success': False, 'error': error}
            return JsonResponse(data, status=500)
