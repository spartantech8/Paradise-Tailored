from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^tailor$', views.tailor),
    url(r'^process_survey$', views.process_survey),
    url(r'^matches$', views.matches),
    url(r'^sample$', views.sample_booking),
]