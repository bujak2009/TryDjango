"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from pages.views import home_view, contact_view, about_view


urlpatterns = [
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('', home_view, name='home'),
    path('home/', home_view),
    path('contact/', contact_view),
    path('admin/', admin.site.urls),
    path('about/', about_view),
    # previously here, now in products.views:
    # path('create/', product_create_view, name='product-list'),
    # path('product/<int:my_id>/', product_detail_view, name='product-detail'),
    # path('product/<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    # path('product/<int:id>/delete/', product_delete_view, name='product-delete'),
    # path('products/', product_list_view, name='product-list'),

]
