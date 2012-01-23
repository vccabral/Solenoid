from django.forms import ModelForm
from SoftwareStories.SoftwareProjects.models import Project, Tabs, TabItem, ProjectViewers, ProjectEditors

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('user',) 

class ViewerForm(ModelForm):
    class Meta:
        model = ProjectViewers
        fields = ('viewer',) 

class EditorForm(ModelForm):
    class Meta:
        model = ProjectEditors
        fields = ('editor',) 

class TabForm(ModelForm):
    class Meta:
        model = Tabs
        exclude = ('parentProject','ordinal','divWidth','divHeight',) 

class TabSiteChartForm(ModelForm):
    class Meta:
        model = Tabs
        exclude = ('title','ordinal','divWidth','divHeight',) 

class TabRenameForm(ModelForm):
    class Meta:
        model = Tabs
        fields = ('title',) 
        
class TabItemForm(ModelForm):
    class Meta:
        model = TabItem
        fields = ('height','width','zindex','top','left','html','parentTabs','pageItem',)
        
    