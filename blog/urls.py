from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posts.views import index, posts
from accounts.views import login, register
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('posts', posts, name='posts'),
    path('login', login, name='login'),
    path('register', register, name='register'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
