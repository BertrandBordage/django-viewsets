from viewsets import ModelViewSet, SLUG
from .models import Example


example_viewset = ModelViewSet(Example, id_pattern=SLUG, namespace='example_app')


class OtherViewSet(ModelViewSet):
    model = Example
    id_pattern = SLUG
    base_url_pattern = 'others'
    base_url_name = 'other'
    namespace = 'other_app'
