from django.conf.urls.defaults import patterns, url
from SoftwareStories.UserCenter.views import landing, accounts_create

urlpatterns = patterns('',
                       url(r'^login/$', landing, name='landing'),
                       url(r'^create/$', accounts_create, name='accounts_create'),
)
