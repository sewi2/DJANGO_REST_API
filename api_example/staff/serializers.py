from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'surname', 'firstname', 'patronymic', 'position', 'description')
