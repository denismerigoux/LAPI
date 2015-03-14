from django.conf.urls import patterns, include, url
from django.contrib import admin
from census.views import home,comptage,cours,addcount

urlpatterns = patterns('census.views',
    # Examples:
    # url(r'^$', 'LAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accueil/$', 'home'),
    url(r'^$', 'home'),
    url(r'^comptage/$', 'comptage'),
    url(r'^cours/(?P<id_cours>\d+)$', 'cours'),
    url(r'^compter/$', 'addcount'),
)
