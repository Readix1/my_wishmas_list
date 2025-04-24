from rest_framework import serializers
from wishlist.models import Liste, ShareRequest

class ListeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liste
        fields = '__all__'
        read_only_fields = ('owner',)


class ShareRequestSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ShareRequest
        fields = ['id', 'liste', 'follower', 'status', 'created_at']
        read_only_fields = ['follower', 'status', 'created_at']
