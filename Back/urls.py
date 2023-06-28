from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('home', HomeViewset, 'home') 
router.register('contact', ContactViewset, 'contacts') 
router.register('about', AboutViewset, 'about')
router.register('Members', MembersViewset, 'members')


urlpatterns = [
    path('api/', include(router.urls))
]



