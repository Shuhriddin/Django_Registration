from django.urls import path
from . import views as user_views
from django.contrib.auth import views as authentication_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profilepage, name='profilepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)