from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('records.urls')),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
