from .BaseSerializer import DynamicFieldsModelSerializer
from apps.task.models import CategoryModel

class CategoryListSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class CategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['task']