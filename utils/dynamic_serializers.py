from rest_framework.serializers import ModelSerializer
class DynamicModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        depth = kwargs.pop('depth',None)
        fields = kwargs.pop('fields',None)
        super().__init__(*args, **kwargs)
        if depth is not None:
            self.Meta.depth = depth
        if fields:
            self.Meta.fields = fields