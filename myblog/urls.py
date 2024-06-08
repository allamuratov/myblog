from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', blog_views.signup, name='signup'),
]
