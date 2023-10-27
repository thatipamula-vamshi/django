from django.urls import path
from . import views

urlpatterns = [
    path('image/',views.uploadimages, name = 'uplaodimages'),
    path('file/',views.uploadfile, name = 'uplaodfile')
]
