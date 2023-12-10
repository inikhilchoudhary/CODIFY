# urls.py

from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('/admin/', admin.site.urls),
    path("", views.index, name='home'),  # Assign the name 'home' to your home view
    path("Subjects", views.subjects, name='subjects'),
    path("SourceCode", views.source_code, name='source_code'),
    path("Contribute", views.contribute, name='contribute'),
    path("AboutUs", views.about_us, name='about_us'),
    path("Contact", views.contact, name='contact'),
    path("TermsAndCondition", views.tandc, name='tandc'),
    path("PrivacyAndPolicy", views.privacyandpolicy, name='privacyandpolicy'),
    path("Projects", views.projects, name='projects'),
    
]
