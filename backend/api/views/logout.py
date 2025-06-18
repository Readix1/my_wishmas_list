from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()  # Supprime le token
        except (AttributeError, Token.DoesNotExist):
            pass
        return Response({"detail": "Déconnexion réussie"}, status=status.HTTP_200_OK)
