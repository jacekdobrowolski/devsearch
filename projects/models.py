from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project(models.Model):
    project_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(default='default.jpg', null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created']


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    review_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=4, choices=VOTE_TYPE)

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    tag_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
