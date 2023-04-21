import uuid

from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    descreption = models.TextField(null=True,blank=True)
    demo_link = models.CharField(null=True, blank=True, max_length=255)
    source_link = models.CharField(max_length=255, null=True,blank=True)
    vote_count = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    tag = models.ManyToManyField('Tag',blank=True)


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class Review(models.Model):
    VOTE_TYPE = (
        ('yaxshi', 'Ijobiy'),
        ('yomon', 'Salbiy')
    )
    body = models.TextField(default='')
    value = models.CharField(max_length=255, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='project_review')


    def __str__(self):
        return self.body



    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'


class Tag(models.Model):
    name = models.CharField(max_length=155)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Telefon'
        verbose_name_plural = 'Telefonlar'
