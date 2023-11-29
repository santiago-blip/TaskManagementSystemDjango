from .BaseSerializer import DynamicFieldsModelSerializer
from apps.task.models import StatusModel

class StatusSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = StatusModel
        fields = '__all__'