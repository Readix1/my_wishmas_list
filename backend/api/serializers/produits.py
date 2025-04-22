from rest_framework import serializers
from wishlist.models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
        read_only_fields = ('added_by',)

