from rest_framework import viewsets, permissions
from wishlist.models import Liste, Produit
from ..serializers.listes import ListeSerializer
from ..permissions import IsOwner

class ListeViewSet(viewsets.ModelViewSet):
    queryset = Liste.objects.all()
    serializer_class = ListeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Liste.objects.filter(owner=self.request.user)