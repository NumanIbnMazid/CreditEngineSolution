from django.urls import re_path
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from rosetta.views import *

ROSETTA_URLS = [
    re_path(
        r'^$',
        RedirectView.as_view(
            url=reverse_lazy('rosetta-file-list',
                             kwargs={'po_filter': 'project'}),
            permanent=False,
        ),
        name='rosetta-old-home-redirect',
    ),
    re_path(
        r'^translations/$',
        RedirectView.as_view(
            url=reverse_lazy('rosetta-file-list',
                             kwargs={'po_filter': 'project'}),
            permanent=False,
        ),
        name='rosetta-file-list-redirect',
    ),
    re_path(
        r'^translations/(?P<po_filter>[\w-]+)/$',
        TranslationFileListView.as_view(),
        name='rosetta-file-list',
    ),
    re_path(
        r'^translations/(?P<po_filter>[\w-]+)/(?P<lang_id>[\w\-_\.]+)/(?P<idx>\d+)/$',
        TranslationFormView.as_view(),
        name='rosetta-form',
    ),
    re_path(
        r'^translations/(?P<po_filter>[\w-]+)/(?P<lang_id>[\w\-_\.]+)/(?P<idx>\d+)/download/$',
        TranslationFileDownload.as_view(),
        name='rosetta-download-file',
    ),
    re_path(r'^translate/$', translate_text,
            name='rosetta.translate_text'),
]
