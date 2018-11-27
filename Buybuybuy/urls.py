"""Buybuybuy URL Configuration

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
from django.urls import path
from django.conf.urls import url,include
from customer import urls as customerurls
from trade import urls as tradeurls
from super import urls as superurls

urlpatterns = [
    path('admin/', admin.site.urls),

    #app super
    url(r'',include(superurls, namespace='super')),
    #app customer
    #url(r'^customer', include(customerurls, namespace="customer")),

    #trade
    #url(r'^trade', include(tradeurls), namespace="trade"),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.UPLOAD_ROOT)
