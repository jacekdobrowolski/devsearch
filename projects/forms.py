from django.forms import ModelForm
from django import forms
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'featured_image',
            'description',
            'tags',
            'demo_link',
            'source_link',
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
