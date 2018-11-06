from django.urls import path

import oauth.views as oauth

urlpatterns = [
    path('', oauth.do_oauth, name='oauth'),
    path('logout/', oauth.log_out, name='logout'),
    path('callback/', oauth.callback, name='callback'),
]
