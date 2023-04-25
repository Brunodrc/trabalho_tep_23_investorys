
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_user/', include('auth_user.urls')),
    path('investments/', include('investments.urls')),
    path('stocks/', include('stocks.urls')),
]
