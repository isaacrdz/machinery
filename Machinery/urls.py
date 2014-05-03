from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Machinery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^equipments/(?P<model>[\w\-/w]+)/', 'equipments.views.equipment_view',name ='equipment_view'),
    url(r'^$', 'equipments.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),


    
)
