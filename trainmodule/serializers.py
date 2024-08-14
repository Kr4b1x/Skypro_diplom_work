from rest_framework import serializers

from .models import TrainModel


class TrainSerializer(serializers.ModelSerializer):
    """
    Serializer for Training model.
    """
    class Meta:
        model = TrainModel
        fields = ["number", "name", "description"]
