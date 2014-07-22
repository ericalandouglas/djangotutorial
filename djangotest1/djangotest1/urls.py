from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
from djangotest1.forms import ContactForm1, ContactForm2, ContactForm3
from djangotest1.views import ContactWizard
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^articles/', include('article.urls')), # urls defined for article app
    (r'^accounts/', include('userprofile.urls')),

    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_template_simpler/$', 'article.views.hello_template_simpler'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    # user auth account urls
    url(r'^accounts/login/$', 'djangotest1.views.login'),
    url(r'^accounts/auth/$', 'djangotest1.views.auth_view'),
    url(r'^accounts/logout/$', 'djangotest1.views.logout'),
    url(r'^accounts/loggedin/$', 'djangotest1.views.loggedin'),
    url(r'^accounts/invalid/$', 'djangotest1.views.invalid_login'),
    url(r'^accounts/register/$', 'djangotest1.views.register_user'),
    url(r'^accounts/register_success/$', 'djangotest1.views.register_success'),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
)

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
