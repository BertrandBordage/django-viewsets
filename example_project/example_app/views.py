from viewsets.model_viewset import ModelViewSet
from .models import Example


class ExampleViewSet(ModelViewSet):
    model = Example
