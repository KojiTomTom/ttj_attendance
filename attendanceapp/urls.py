from django.urls import path, include
from .views import calendar_views, index_views, seat_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index_views.initialize, name='initialize'),
    path('check-selection/', index_views.checkSelection, name='check_selection'),
    path('calendar/', calendar_views.initialize, name='calendar_view'),
    path('calendar/check/', calendar_views.reserve_check, name='reserve_check'),
    path('calendar/cancel/', calendar_views.cancel_reservation, name='cancel_reservation'),
    path('calendar/month_change/', calendar_views.month_change, name='month_change'),
    path('seat/', seat_view.initialize, name='seat_view'),        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
