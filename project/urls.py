"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from photo_gallery_aaron import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
# Photo urls
    path('photo/detail/', views.photo_detail, name='photo_detail'),
    path('photo/upload_photo/', views.upload_photo, name='upload_photo'),
    path('photo/delete_photo/', views.delete_photo, name='delete_photo'),
    path('photo/photo_comment/', views.photo_comment, name='photo_comment'),

#Gallery urls
    path('gallery/add/', views.add_gallery, name='add_gallery'),
    path('gallery/view/', views.view_gallery, name='view_gallery'),
    path('gallery/edit', views.edit_gallery, name='edit_gallery'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns