"""scr URL Configuration

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

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
 
from pages.views import home_view, about_view, contact_view

from account.views import login_view, logout_view, register_view   

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),

    
    path('__debug__/', include('debug_toolbar.urls')),
    path('polls/', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('products/', include('products.urls')),
    path('myfourthapp/', include('myfourthapp.urls')),
	path('', home_view, name='home'),
	path('about/<int:year>/<int:month>/<int:day>/', about_view, name='product-detail'),
	path('contact/', contact_view),
    path('admin/', admin.site.urls),
]
