from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^open_match/$', views.open_match),
	url(r'^match_list/$', views.match_list),
	url(r'^send_coefs_ajax/$', views.send_coefs_ajax),
	url(r'^generate_page/$', views.generate_page, name='generate_page'),
	url(r'^match_list/$', views.match_list, name='match_list')
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/', include(debug_toolbar.urls)),
	]
