import os.path

from django.views.generic import TemplateView, RedirectView

from django.conf.urls import patterns, include, url

from django.contrib import admin

from elmusico.views import *
from rotten.views import *
from rotten.views_dev import *
from zhing.views import *
from chin.views import *
from moodring.views import *
from mapler.views import *
admin.autodiscover()

site_media = os.path.join(
    os.path.dirname(__file__), '../site_media'
)
rotten_csv = os.path.join(
    os.path.dirname(__file__), '../rotten/csv'
)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elmusico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', main_page),
    # (r'^$', maintaining),
    # \w: alphanumeric characters with underscore
    # (r'^user/(\w+)/$', user_page),
    # # session manager part
    # (r'^login/$', 'django.contrib.auth.views.login'),
    # (r'^logout/$', logout_page),
    # (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    # (r'^rotten_csv/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': rotten_csv }),
    # (r'^register/$', register_page),
    # (r'^register/success/$',
    #     TemplateView.as_view(template_name='registration/register_success.html')),
    # # DML part
    # (r'^create_artist/$', artist_save_page),
    # (r'^search_member/(\w+)/$', search_member_page),
    # (r'^relation/(\w+)/$', relation_page),
    # (r'^create_album/$', album_save_page),
    # (r'^create_song/$', song_save_page_step1),
    # (r'^create_song_step2/(\w+)/$', song_save_page_step2),
    # (r'^create_video/$', video_save_page_step1),
    # (r'^create_video_step2/(\w+)/$', video_save_page_step2),
    # (r'^create_tab/$', tab_save_page_step1),
    # (r'^create_tab_step2/(\w+)/$', tab_save_page_step2),
    # # querry part
    # (r'^search/$', search_page),
    # (r'^album/(\w+)/$', album_page),
    # (r'^artist/(\w+)/$', artist_page),
    # (r'^song/(\w+)/$', song_page),
    # (r'^tab/(\w+)/$', tab_page),
    # rotten
    (r'^rotten/$', rotten_page),
    (r'^rotten/similar/(\w+)$', rotten_similar),
    (r'^rotten_dev/$', rotten_page_dev),
    (r'^rotten_dev/similar/(\w+)$', rotten_similar_dev),
    # chin
    (r'^chin/$', chin),
    (r'^mapler/$', mapler),
    # (r'^search/$', create_album),

    url(r'^admin/', include(admin.site.urls)),
)
