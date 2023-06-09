from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views


urlpatterns = [
    path('',blog_views.PostListView.as_view(),name="home page"),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('users/',include('users.urls')),
    path('register/',users_views.register, name="register-view"),
    path('profile/',users_views.profile, name="profile-view"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login-view'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout-view'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
