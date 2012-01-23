from django.db import models
from SoftwareStories.WebDrawing.models import PageItem
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User,editable=False)
    title = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return self.title
    
class Tabs(models.Model):
    parentProject = models.ForeignKey(Project,editable=False)
    parentTab = models.ForeignKey('self',blank=True,null=True,default=None)
    title = models.CharField(max_length=200)
    ordinal = models.IntegerField(default=1,editable=False)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["ordinal"]
        unique_together = ('parentProject', 'title',)
    def __str__(self):
        return self.title
    
class TabItem(models.Model):
    parentTabs = models.ForeignKey(Tabs)
    pageItem = models.ForeignKey(PageItem)
    top = models.IntegerField(default=50)
    left = models.IntegerField(default=50)
    width = models.IntegerField(default=200)
    height = models.IntegerField(default=200)
    zindex = models.IntegerField(default=1)
    html = models.CharField(max_length=1000,default='',blank=True)
    updated = models.DateTimeField(auto_now=True)
    def toCSS(self):
        #this is direct css
        return "background: url('/static/images/"+str(self.pageItem.stockImage)+"') no-repeat; background-size: 100%; top: "+str(self.top)+"; left: "+str(self.left)+"; width: "+str(self.width)+"; height: "+str(self.height)
    def __str__(self):
        return self.id
    
class ProjectViewers(models.Model):
    viewer = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('viewer', 'project',)
    def __str__(self):
        return self.viewer.username
    
class ProjectEditors(models.Model):
    editor = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('editor', 'project',)
    def __str__(self):
        return self.editor.username
    