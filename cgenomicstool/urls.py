from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include("pages.urls")),
    path('tools/crosstab/', include("crosstab.urls")),
    path('admin/', admin.site.urls),
]
