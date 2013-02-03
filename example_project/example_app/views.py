from viewsets import ModelViewSet, SLUG
from .models import Example


other_example_viewset = ModelViewSet(Example, id_pattern=SLUG)


class ExampleViewSet(ModelViewSet):
    model = Example
    id_pattern = SLUG
    base_url_pattern = 'others'
    base_url_name = 'other'
