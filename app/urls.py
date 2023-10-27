from django.urls import path
#from app.views import hello, job_details
from app import views

urlpatterns =[
    path ('', views.job_list, name = 'home'),
    path ('job/<int:id>', views.job_details, name = 'details'),
    path ( 'hello/', views.hello,name = 'hello'),
]