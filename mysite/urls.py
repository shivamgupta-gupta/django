"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from polls import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^purchase/$',views.purchase),
    url(r'^purchase/charoli/$',views.charoli),
    url(r'^purchase/almonds/$',views.almonds),
    url(r'^purchase/aniseed/$',views.aniseed),
    url(r'^purchase/anjir/$',views.anjir),
    url(r'^purchase/apricots/$',views.apricots),
    url(r'^purchase/bayleaf/$',views.bayleaf),
    url(r'^purchase/blackcardamom/$',views.blackcardamom),
    url(r'^purchase/blackcumin/$',views.blackcumin),
    url(r'^purchase/blackpepper/$',views.blackpepper),
    url(r'^purchase/cashew/$',views.cashew),
    url(r'^purchase/coconutpowder/$',views.coconutpowder),
    url(r'^purchase/contact_us/$',views.contact_us),
    url(r'^purchase/elaichi/$',views.elaichi),
    url(r'^purchase/fruitnuts/$',views.fruitnuts),
    url(r'^purchase/hing/$',views.hing),
    url(r'^purchase/kalimirch/$',views.kalimirch),
    url(r'^purchase/kesar/$',views.kesar),
    url(r'^purchase/khajur/$',views.khajur),
    url(r'^purchase/milkpowder/$',views.milkpowder),
    url(r'^purchase/pista/$',views.pista),
    url(r'^purchase/plum/$',views.plum),
    url(r'^purchase/raisins/$',views.raisins),
    url(r'^purchase/redchilli/$',views.redchilli),
    url(r'^purchase/whitepepper/$',views.whitepepper),
    url(r'^contact_us/$',views.contact_us),
]
