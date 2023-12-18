from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('hello', views.indexRender),
    path('itmo', views.universityInfo),
    path('discipline', views.disciplineInfo),
    path('group', views.groupsInfo),
    path('departments', views.departmentsInfo),
    path('structure', views.universityStructure)
]