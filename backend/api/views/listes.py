from rest_framework import viewsets, permissions
from wishlist.models import Liste, ShareRequest
from ..serializers.listes import ListeSerializer, ShareRequestSerializer, ListeSerializer
from ..permissions import IsOwner
from rest_framework import generics, permissions, status, views
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ListeViewSet(viewsets.ModelViewSet):
    queryset = Liste.objects.all()
    serializer_class = ListeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Liste.objects.filter(owner=self.request.user)
    
class ListeJoinDetailView(generics.RetrieveAPIView):
    queryset = Liste.objects.all()
    serializer_class = ListeSerializer
    lookup_field = 'share_token'
    permission_classes = [permissions.IsAuthenticated]
    
    
# ✉️ POST /api/listes/join/<uuid>/
# Créer une demande d’accès à une liste
class CreateShareRequestView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, token):
        try:
            liste = Liste.objects.get(share_token=token)
        except Liste.DoesNotExist:
            raise NotFound("Liste non trouvée")

        if liste.owner == request.user:
            raise PermissionDenied("Tu es déjà le propriétaire de cette liste.")

        if ShareRequest.objects.filter(liste=liste, follower =request.user).exists():
            return Response({"detail": "Demande déjà envoyée."}, status=400)

        share_request = ShareRequest.objects.create(
            liste=liste,
            follower =request.user
        )
        serializer = ShareRequestSerializer(share_request)
        return Response(serializer.data, status=201)
    
    
# 📬 GET /api/demandes/
# Liste des demandes reçues par l’utilisateur (en tant que propriétaire)
class ShareRequestListView(generics.ListAPIView):
    serializer_class = ShareRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShareRequest.objects.filter(liste__owner=self.request.user)


class AcceptShareRequestView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        demande = get_object_or_404(ShareRequest, pk=pk)

        if demande.liste.owner != request.user:
            raise PermissionDenied("Tu n'as pas le droit de faire ça.")

        if demande.status != 'pending':
            return Response({"detail": "Demande déjà traitée."}, status=400)

        demande.status = 'accepted'
        demande.save()
        # demande.liste.shared_with.add(demande.follower)

        return Response({"detail": "Demande acceptée."})


class RefuseShareRequestView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        demande = get_object_or_404(ShareRequest, pk=pk)

        if demande.liste.owner != request.user:
            raise PermissionDenied("Tu n'as pas le droit de faire ça.")

        if demande.status != 'pending':
            return Response({"detail": "Demande déjà traitée."}, status=400)

        demande.status = 'refused'
        demande.save()

        return Response({"detail": "Demande refusée."})


from rest_framework import generics
from django.contrib.auth import get_user_model
from ..serializers.user import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

CustomUser = get_user_model()

class ListeMembresView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        liste_id = self.kwargs['pk']
        try:
            liste = Liste.objects.get(pk=liste_id)
            
        except Liste.DoesNotExist:
            raise NotFound("Liste introuvable.")


        if liste.owner != self.request.user:
            raise PermissionDenied("Tu n'as pas accès à ces membres.")

        # 🔽 Liste des utilisateurs ayant une demande acceptée
        return CustomUser.objects.filter(
            sharerequest__liste=liste,
            sharerequest__status='accepted'
        )


class ListeDemandesView(generics.ListAPIView):
    serializer_class = ShareRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        liste_id = self.kwargs['pk']
        try:
            liste = Liste.objects.get(pk=liste_id)
        except Liste.DoesNotExist:
            raise NotFound("Liste introuvable.")

        if liste.owner != self.request.user:
            raise PermissionDenied("Tu n'as pas accès aux demandes de cette liste.")

        return liste.demandes.all()
