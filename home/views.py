import logging
import requests
import urllib
from urllib.parse import urlencode
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from home.models import Social, Settings, About
from oauth.models import Oauth

logger = logging.getLogger('app')
config = settings.CONFIG


def home_view(request):
    # View: /
    return render(request, 'home.html')


def about_view(request):
    # View: /about/
    data = {'social': Social.objects.all(), 'about': About.objects.all()[0]}
    return render(request, 'about.html', {'data': data})


def romhacks_view(request):
    # View: /romhacks/
    return render(request, 'romhacks.html')


def speedrun_view(request):
    # View: /speedruns/
    return render(request, 'speedruns.html')


@login_required
def members_view(request):
    # View: /members/
    return render(request, 'members.html')


def get_m3u8(request):
    user_settings = Settings.objects.all()[0]
    oauth = Oauth.objects.all()[0]
    token_url = 'https://api.twitch.tv/api/channels/{}/access_token'.format(
        user_settings.twitch_username
    )
    headers = {'Client-ID': oauth.client_id}
    r = requests.get(token_url, headers=headers, timeout=10)
    j = r.json()
    uri = 'http://usher.twitch.tv/api/channel/hls/{}.m3u8'.format(
        user_settings.twitch_username
    )
    data = {
        'player': 'twitchweb',
        'token': j['token'],
        'sig': j['sig'],
        'allow_audio_only': 'true',
        'allow_source': 'true',
        'type': 'any',
        'p': '1234',
    }
    params = urllib.parse.urlencode(data)
    url = '{}?{}'.format(uri, params)
    return HttpResponseRedirect(url)
