from django.urls import path

import home.views as home

urlpatterns = [
    path('', home.home_view, name='home_view'),
    path('about/', home.about_view, name='about_view'),
    path('romhacks/', home.romhacks_view, name='romhacks_view'),
    path('speedruns/', home.speedrun_view, name='speedrun_view'),
    path('members/', home.members_view, name='members_view'),
    path('hls/', home.get_m3u8, name='get_m3u8'),
]
