from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from clothes.views import index, about, contact, shop, shop_single, filter_shop, login, GoodsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fami/', index),
    path('about/', about),
    path('contact/', contact),
    path('fami/shop/', GoodsAPIView.as_view()),
    path('fami/shop/<slug:cat_slug>', filter_shop),
    path('fami/shop-single/<slug:goods_slug>', shop_single),
    path('fami/login', login),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
