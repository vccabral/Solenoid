from SoftwareStories.SoftwareProjects.models import User
from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm

class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )
        
