from django.urls import path
from .views import MessageViesSet, MessageCreateViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'chat'
urlpatterns = format_suffix_patterns([
    path('api/messages/list/', MessageViesSet.as_view({'get': 'list'})),
    path('api/messages/single/<int:pk>/', MessageViesSet.as_view({'get': 'retrieve'})),
    path('api/messages/add/', MessageCreateViewSet.as_view({'post': 'create'}))
])
