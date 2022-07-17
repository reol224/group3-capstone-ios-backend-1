from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from inspect import getmembers
from types import FunctionType


def attributes(obj):
    disallowed_names = {
        name for name, value in getmembers(type(obj))
        if isinstance(value, FunctionType)}
    return {
        name: getattr(obj, name) for name in dir(obj)
        if name[0] != '_' and name not in disallowed_names and hasattr(obj, name)}


class CustomDefaultPagination(PageNumberPagination):
    page_size_query_param = "pageSize"
    page_query_param = "page"

    def get_paginated_response(self, data):
        return Response({
            'current_page': self.page.number,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            # 'page_range': [x for x in self.page.paginator.page_range],
            'per_page': self.page.paginator.per_page,
            'results': data,
        })
