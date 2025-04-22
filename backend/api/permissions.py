from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Autorise uniquement les propriétaires à modifier ou supprimer.
    Lecture seule sinon.
    """

    def has_object_permission(self, request, view, obj):
        # Si le modèle a un champ 'owner'
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        
        # Si c’est un produit, on vérifie la liste.owner
        if hasattr(obj, 'liste'):
            return obj.liste.owner == request.user
        
        return False
