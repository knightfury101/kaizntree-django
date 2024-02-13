from drf_yasg import openapi

list_products_parameters = [
    openapi.Parameter(
        name='name_contains',
        in_=openapi.IN_QUERY,
        description='Filter by product name containing specified string',
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        name='category',
        in_=openapi.IN_QUERY,
        description='Filter by category name',
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        name='tags',
        in_=openapi.IN_QUERY,
        description='Filter by tags (comma-separated list)',
        type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        name='stock_status_min',
        in_=openapi.IN_QUERY,
        description='Minimum stock status',
        type=openapi.TYPE_INTEGER
    ),
    openapi.Parameter(
        name='stock_status_max',
        in_=openapi.IN_QUERY,
        description='Maximum stock status',
        type=openapi.TYPE_INTEGER
    ),
    openapi.Parameter(
        name='available_stock_min',
        in_=openapi.IN_QUERY,
        description='Minimum available stock',
        type=openapi.TYPE_INTEGER
    ),
    openapi.Parameter(
        name='available_stock_max',
        in_=openapi.IN_QUERY,
        description='Maximum available stock',
        type=openapi.TYPE_INTEGER
    ),
]
