from django.urls import path
from .views import *


urlpatterns = [
    path('projects/', projects, name='projects'),
    path('projects/<uuid:id>', project, name='project'),
    path('projects_add/', project_add, name='project_add'),
    path('projects_edit/<uuid:id>', project_edit, name='project_edit')
]