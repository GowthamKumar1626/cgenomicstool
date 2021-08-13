from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


API_TITLE = 'CGenomicsTool API'
API_DESCRIPTION = 'A Web API for tools used in studying comparative Genomics'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    url(r'^', include('base.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)