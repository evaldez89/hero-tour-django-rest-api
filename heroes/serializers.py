from .models import Hero
from rest_framework import serializers


class HeroSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    super_power = serializers.CharField(required=True)
    strength = serializers.IntegerField(required=True)
    inserted_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Hero.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        from pprint import pprint as pp
        pp(validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.super_power = validated_data.get('super_power', instance.super_power)
        instance.strength = validated_data.get('strength', instance.strength)
        instance.save()
        return instance