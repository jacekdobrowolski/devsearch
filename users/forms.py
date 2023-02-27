from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from users.models import Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'username',
            'password1',
            'password2',
        ]
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
