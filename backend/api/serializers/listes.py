from rest_framework import serializers
from wishlist.models import Liste

class ListeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liste
        fields = '__all__'
        read_only_fields = ('owner',)

