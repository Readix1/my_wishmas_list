from rest_framework import viewsets, permissions
from wishlist.models import Liste, Produit
from ..serializers.produits import ProduitSerializer
from ..permissions import IsOwner

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_queryset(self):
        return Produit.objects.filter(liste__owner=self.request.user)