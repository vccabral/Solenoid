from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from SoftwareStories.SoftwareProjects.models import Project, ProjectViewers, ProjectEditors, Tabs, TabItem
from SoftwareStories.SoftwareProjects.forms import ProjectForm, ViewerForm, EditorForm, TabForm, TabItemForm, TabSiteChartForm
from SoftwareStories.WebDrawing.models import PageItem, SoftwareStory


@login_required
def project_create(request):
    if(request.method == 'POST'):
        projectForm = ProjectForm(request.POST)
        if(projectForm.is_valid()):
            project = projectForm.save(commit=False)
            project.user = request.user
            project.save()
            projectForm = ProjectForm()
            return HttpResponseRedirect("/project/list/")
    else:
        projectForm = ProjectForm()            
    projectList = Project.objects.filter(user=request.user)
    return render_to_response("Project.sub",RequestContext(request,locals()))

@login_required
def projects_read(request):
    projectForm = ProjectForm()
    projectList = Project.objects.filter(user=request.user)
    return render_to_response("Projects.html",RequestContext(request,locals()))

@login_required
def project_read(request,id):
    curProject = get_object_or_404(Project,pk=id)
    projectForm = ProjectForm()
    viewerForm = ViewerForm()
    editorForm = EditorForm()
    projectList = Project.objects.filter(user=request.user)
    projectViewList = ProjectViewers.objects.filter(project=curProject)
    projectEditList = ProjectEditors.objects.filter(project=curProject)
    return render_to_response("Project.html",RequestContext(request,locals()))

@login_required
def project_update(request):
    return render_to_response("Project.html",RequestContext(request,locals()))

@login_required
def project_delete(request,id):
    return render_to_response("Project.html",RequestContext(request,locals()))

#login_required
def viewer_delete(request,id):
    
    return render_to_response("ProjectViewer.sub",RequestContext(request,locals()))

@login_required
def viewer_create(request,id):
    curProject = get_object_or_404(Project,pk=id)
    if(request.method == 'POST'):
        viewerForm = ViewerForm(request.POST)
        if(viewerForm.is_valid()):
            viewer = viewerForm.save(commit=False)
            viewer.project = curProject
            viewer.save()
            viewerForm = ViewerForm()
    projectViewList = ProjectViewers.objects.filter(project=curProject)
    return render_to_response("ProjectViewer.sub",RequestContext(request,locals()))

@login_required
def editor_create(request,id):
    curProject = get_object_or_404(Project,pk=id)
    if(request.method == 'POST'):
        editorForm = EditorForm(request.POST)
        if(editorForm.is_valid()):
            editor = editorForm.save(commit=False)
            editor.project = curProject
            editor.save()
            editorForm = EditorForm()
    projectEditList = ProjectEditors.objects.filter(project=curProject)
    return render_to_response("ProjectEditor.sub",RequestContext(request,locals()))

@login_required
def project_canvas(request,id):
    curProject = get_object_or_404(Project,pk=id)
    addablePageItems = PageItem.objects.all()
    tabs = Tabs.objects.filter(parentProject=curProject).select_related()
    tabForm = TabForm()
    tabItemForm = TabItemForm()
    return render_to_response("Canvas.html",RequestContext(request,locals()))

@login_required
def tab_create(request,id):
    curProject = get_object_or_404(Project,pk=id)
    if(request.method == 'POST'):
        tabForm = TabForm(request.POST)
        if(tabForm.is_valid()):
            tab = tabForm.save(commit=False)
            tab.parentProject = curProject
            tab.save()
            tabForm = TabForm()
    return render_to_response("Tab.form",RequestContext(request,locals()))
    
@login_required
def tabitem_update(request, id, tabItemId):
    curProject = get_object_or_404(Project,pk=id)
    if(request.method == 'POST'):
        tabItemForm = TabItemForm(request.POST, instance = get_object_or_404(TabItem,pk=tabItemId))
        if(tabItemForm.is_valid()):
            tabItemForm.save()
            return render_to_response("ok.json",RequestContext(request,{'pk_id': tabItemId}))
    return render_to_response("fail.json",RequestContext(request,{'pk_id': '-1'}))

@login_required
def tabitem_create(request, id):
    curProject = get_object_or_404(Project,pk=id)
    if(request.method == 'POST'):
        tabItemForm = TabItemForm(request.POST)
        if(tabItemForm.is_valid()):
            tabItem = tabItemForm.save()
            return render_to_response("ok.json",RequestContext(request,{'pk_id': tabItem.id}))
    return render_to_response("fail.json",RequestContext(request,{'pk_id': '-1'}))

@login_required
def sitemap_read(request, id):
    curProject = get_object_or_404(Project,pk=id)
    tabs = Tabs.objects.filter(parentProject=curProject).select_related()
    tabSiteChartForm = TabSiteChartForm()
    return render_to_response("SiteMap.html",RequestContext(request,locals()))

@login_required
def tab_update(request, id, tabId):
    curProject = get_object_or_404(Project,pk=id)
    if(request.method == 'POST'):
        tabSiteChartForm = TabSiteChartForm(request.POST,instance=get_object_or_404(Tabs,pk=tabId))
        if tabSiteChartForm.is_valid():
            t = tabSiteChartForm.save()
            return render_to_response("ok.json",RequestContext(request,{'pk_id': tabId}))
    return render_to_response("fail.json",RequestContext(request,{'pk_id': -1}))

@login_required
def stories_read(request, id):
    #fix me, way to many queries
    curProject = Project.objects.select_related().get(pk=id)
    storyList = {}
    hoursTotal = 0
    for tab in Tabs.objects.filter(parentProject=curProject):
        for tabItem in TabItem.objects.filter(parentTabs=tab):
            for oneStory in PageItem.objects.filter(id=tabItem.pageItem.id).stories:
                storyList[oneStory.id] = oneStory.estimatesHours 
                hoursTotal = oneStory.estimatesHours
    return render_to_response("ManHours.html",RequestContext(request,locals()))
    