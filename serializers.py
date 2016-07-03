from rest_framework import serializers
from server.model import Test


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('title', 'message')