from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('login/', auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('post.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
