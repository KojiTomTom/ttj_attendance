from django.urls import path, include
from .views import index_views, reservation_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_views.initialize, name='initialize'),
    path('check-selection/', index_views.checkSelection, name='check_selection'),
    path('reservation/', reservation_views.initialize, name='reservation_view'),
    path('reservation/check/', reservation_views.reserve_check, name='reserve_check'),
    path('reservation/cancel/', reservation_views.cancel_reservation, name='cancel_reservation'),
    path('reservation/month_change/', reservation_views.month_change, name='month_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
