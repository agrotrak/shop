from django.conf.urls import patterns, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from inetshop.views.default import main,nofound,report_load_xml
from inetshop.views.test import test1,test2,login,logout,form1

urlpatterns = patterns('',
    # Examples:
    url(r'^accounts/logout$',logout),
     url(r'^accounts/login/$',login),
     url(r'^test1$',test1),
     url(r'^test2$',test2),
     url(r'^form1$',form1),
     url(r'^$', nofound ),
     url(r'^main$', main ),
     url(r'^report_load_xml$',report_load_xml),
    # url(r'^point/', include('point.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
