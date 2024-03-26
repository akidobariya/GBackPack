"""
URL configuration for websiteone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings  
from django.conf.urls.static import static  
from application import views


# admin.site.site_header = 'GBACKPACK'                    
# admin.site.index_title = 'GBACKPACK Admin'                 
# admin.site.site_title = 'website for bags'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('shop',views.shop),
    path('blog',views.blog),
    
    path('contact',views.contact),
    path('contactdata',views.contactdata1),

    path('myaccount',views.myaccount),
    path('register', views.registerdata1),

    path('signup',views.signup),
    path('logindata', views.logincheck),

    path('cart',views.cart),
    path('blogone',views.blogone),
    path('blogtwo',views.blogtwo),
    path('blogthree',views.blogthree),
    path('blogfour',views.blogfour),
    path('blogfive',views.blogfive),
    path('blogsix',views.blogsix),

    path('cartdata',views.cartdata),
    path('deletedata',views.deletedata),

    path('increase',views.add),
    path('decrease',views.subtraction),

    path('forgotpassword',views.forgotpassword1),
    path('updatepassword',views.updatepassword1),

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 