from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='Home'),
    path("Subjects",views.subjects,name='Subjects'),
    path("SourceCode",views.source_code,name='SourceCode'),
    path("Contribute",views.contribute,name='Contribute'),
    path("AboutUs",views.about_us,name='AboutUs'),

]
