from myapp.views import*
from django.contrib import admin
from myapp import views as v
from django.contrib.statifiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('/', view=index, name='index'),
]
urlpatterns += staticfiles_urlpatterns()
