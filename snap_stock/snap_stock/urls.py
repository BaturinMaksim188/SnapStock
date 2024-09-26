from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from photos.views import signup as photos_signup



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photos.urls', namespace='photos')),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', photos_signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
