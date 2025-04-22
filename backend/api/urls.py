from rest_framework.routers import DefaultRouter
from .views.listes import ListeViewSet
from .views.produits import ProduitViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'listes', ListeViewSet, basename='liste')
router.register(r'produits', ProduitViewSet, basename='produit')

urlpatterns = router.urls


# urlpatterns += [
#     path('api/', include('api.urls')),
#     path('api-auth/', include('rest_framework.urls')),  # pour le login dans l'interface web
#     path('api/token/', obtain_auth_token),              # endpoint pour obtenir un token
# ]