from viewsets.model import ModelViewSet
from .models import Example


class ExampleViewSet(ModelViewSet):
    model = Example
    excluded_views = ('delete_view',)


other_example_viewset = ModelViewSet(Example, base_url_pattern='others',
                                     base_url_name='other')
