from django.contrib import admin
from django.urls import path, include
from interview import views,api_views

#from iv.api_views import EmailCreate
from rest_framework import routers



#router = routers.DefaultRouter()
#router.register(r'people',api_views.create_person_view, 'people')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.home, name= 'home'),
    #path('test/',views.test, name= 'test'),
    path('', include('interview.urls')),
    #path('api/',api_views.EmailCreate.create_person_view, name = 'api'),
    path('api/subscribe/',api_views.EmailCreate.create_subscribe_view, name = 'subscribe'),
    
]