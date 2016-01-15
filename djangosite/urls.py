from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

PAGE = "<html><body>%s</body></html>"
def home(request): return HttpResponse( PAGE % "Hello World!")

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home, name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^buyme/', include('buyme.urls')),
]
