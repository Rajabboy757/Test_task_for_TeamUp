from rest_framework import serializers
from .models import Test


class IQTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('login', 'IQ_result')
