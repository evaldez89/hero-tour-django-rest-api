from .models import Hero
from rest_framework import serializers


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'super_power', 'strength', 'inserted_on', 'updated_on')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     print("created!!!!!!!")
    #     return Hero.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     print("updated!!!!!!!")
    #     from pprint import pprint as pp
    #     pp(validated_data)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.super_power = validated_data.get('super_power', instance.super_power)
    #     instance.strength = validated_data.get('strength', instance.strength)
    #     instance.save()
    #     return instance