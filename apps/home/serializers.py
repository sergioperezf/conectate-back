from rest_framework import serializers
from apps.home.models import *

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class PedagogicStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = PedagogicStrategy
        fields = '__all__'


class ExampleSerializer(serializers.ModelSerializer):
    discipline = serializers.PrimaryKeyRelatedField(many=False, queryset=Discipline.objects.all())
    pedagogic_strategy = serializers.PrimaryKeyRelatedField(many=False, queryset=PedagogicStrategy.objects.all())
    class Meta:
        model = Example
        fields = '__all__'

    def create(self, validated_data):
        example = Example.objects.create(**validated_data)
        return example


class ToolSerializer(serializers.ModelSerializer):
    tutorials = TutorialSerializer(many=True, read_only=True)
    examples = ExampleSerializer(many=True, read_only=True)
    class Meta:
        model = Tool
        fields = '__all__'