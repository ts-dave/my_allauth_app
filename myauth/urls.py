from django.contrib import admin
from django.urls import path, include
from accounts import views
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('__debug__/', include(debug_toolbar.urls)),
]

