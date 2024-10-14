from django.urls import path
from .views import *
from user.views import *

urlpatterns = [
    path('', homepageView, name='home'),
    path('curriculum',Curriculum.as_view(),name='curriculum'),
    path('contact',ContactView.as_view(),name='contact'),
    path('lifeatwisdom',LifeAtWisdom.as_view(),name='lifeatwisdom'),
    path('toppers',toppersView,name='toppers'),
    path('gallery',GalleryView.as_view(),name='gallery'),
    path('gallery/classrooms',classroomsView,name='classrooms'),
    path('gallery/sports',sportsView,name='sports'),
    path('gallery/events',eventView,name='events'),
    path('gallery/competitions=',competitionsView,name='competitions'),
    path('gallery/graduation',graduationView,name='graduation'),
    path('gallery/schooltrips',schoolTripView,name='schooltrips'),
    path('gallery/pe',peView,name='pe'),
]
