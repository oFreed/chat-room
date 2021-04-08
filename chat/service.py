from django_filters import rest_framework as filter
from rest_framework.response import Response

from .models import Message
from rest_framework.pagination import PageNumberPagination


class PaginationMessages(PageNumberPagination):
    """Paginator settings"""
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'result': data
        })


class MessageFilter(filter.FilterSet):
    """Adding filter to search message by author username"""
    username = filter.CharFilter(field_name='author')

    class Meta:
        model = Message
        fields = ['username', ]
