from rest_framework import viewsets


class ModelViewSet(viewsets.ModelViewSet):
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
