from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from SoftwareStories.WebDrawing.models import *
from SoftwareStories.UserCenter.models import *
from SoftwareStories.SoftwareProjects.models import *

admin.site.register(TabItem)
admin.site.register(Category)
admin.site.register(PageItem)
admin.site.register(SoftwareStory)
admin.site.register(Project)
admin.site.register(ProjectEditors)
admin.site.register(ProjectViewers)
admin.site.register(Tabs)
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^project/', include('SoftwareProjects.urls')),
                       url(r'^accounts/', include('UserCenter.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
