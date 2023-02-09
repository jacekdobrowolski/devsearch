from django.forms import ModelForm
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
