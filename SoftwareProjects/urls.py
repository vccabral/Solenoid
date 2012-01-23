from django.conf.urls.defaults import patterns, url
from SoftwareStories.SoftwareProjects.views import project_create, project_read, projects_read, project_update, project_delete, editor_create, viewer_create, project_canvas, tab_create, tabitem_update, tabitem_create, sitemap_read, tab_update, stories_read, viewer_delete

urlpatterns = patterns('',
                       url(r'^create/$', project_create, name='project_create'),
                       url(r'^list/$', projects_read, name='projects_read'),
                       url(r'^(\d+)/$', project_read, name='project_read'),
                       url(r'^(\d+)/map/$', sitemap_read, name='sitemap_read'),
                       url(r'^(\d+)/update/$', project_update, name='project_update'),
                       url(r'^(\d+)/delete/$', project_delete, name='project_delete'),
                       url(r'^(\d+)/viewer/create/$', viewer_create, name='viewer_create'),
                       url(r'^(\d+)/viewer/(\d+)/delete/$', viewer_delete, name='viewer_delete'),
                       url(r'^(\d+)/editor/create/$', editor_create, name='editor_create'),
                       url(r'^(\d+)/canvas/$', project_canvas, name='project_canvas'),
                       url(r'^(\d+)/tab/create/$', tab_create, name='tab_create'),
                       url(r'^(\d+)/tab/update/(\d+)/$', tab_update, name='tab_update'),
                       url(r'^(\d+)/tabitem/create/$', tabitem_create, name='tabitem_create'),
                       url(r'^(\d+)/tabitem/(\d+)/update/$', tabitem_update, name='tabitem_update'),
                       url(r'^(\d+)/stories/$', stories_read, name='stories_read'),
)
