
from django.urls import path 

from . import views

app_name = 'theblog'

urlpatterns = [
    
    path('', views.postlist , name= 'postlist' ),
    path('<int:id>/', views.postdetail , name= 'postdetail' ),
]
