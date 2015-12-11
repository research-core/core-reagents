from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reagents_db.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/', include('allauth.urls')),
	url(r'^', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns = patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns