from rest_framework import serializers
from . import models


class ContentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Contents
        fields = '__all__'
