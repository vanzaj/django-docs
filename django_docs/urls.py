from django.conf.urls import patterns, url
from .views import DocsRootView, serve_docs

urlpatterns = patterns(
    '',
    url(r'^$', DocsRootView.as_view(), name='docs_root'),
    url(r'^(?P<path>.*)$', serve_docs, name='docs_files'),
)
