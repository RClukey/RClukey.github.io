from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('metalearth', views.metalearth, name='metalEarth'),
    path('metalearth/<str:name>', views.sculpture, name='sculpture'),
    path('resume', views.resume, name='resume'),
    path('youtube', views.youtube, name='youtube'),
    path('<str:viewer>/view', views.viewPDF, name='PDFviewer'),
]