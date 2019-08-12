from rest_framework import serializers
from sounds.models import Category, SoundByte


class SoundByteSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = SoundByte
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    soundbyte_set = SoundByteSerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"
