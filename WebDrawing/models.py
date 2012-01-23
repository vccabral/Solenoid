from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos')
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class SoftwareStory(models.Model):
    desc = models.CharField(max_length=500)
    estimatesHours = models.IntegerField()
    complexityFactor = models.FloatField()
    doubleCount = models.BooleanField(default=False)
    def __str__(self):
        return self.desc
    
class PageItem(models.Model):
    stockImage = models.ImageField(upload_to='photos')
    previewImage = models.ImageField(upload_to='photos')
    cssName = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    top = models.IntegerField(default=0)
    left = models.IntegerField(default=0)
    width = models.IntegerField(default=200)
    height = models.IntegerField(default=200)
    zindex = models.IntegerField(default=1)
    html = models.CharField(max_length=200,default='')
    updated = models.DateTimeField(auto_now=True)
    stories = models.ManyToManyField(SoftwareStory)
    complexityFactor = models.FloatField()
    def __str__(self):
        return self.title
    def toCSS(self):
        #this is direct css
        return "background: url('/static/images/"+str(self.stockImage)+"') no-repeat; background-size: 100%; top: "+str(self.top)+"; left: "+str(self.left)+"; width: "+str(self.width)+"; height: "+str(self.height)

