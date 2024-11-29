from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login at root
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Add logout functionality
    path('test/', include('test_app.urls')),  # Test app
]
