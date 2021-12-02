from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('post/<str:pk>',views.post, name='post'),
    path('about/',views.about,name='about')
]