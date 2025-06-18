from rest_framework.routers import DefaultRouter
from .views.listes import (ListeViewSet, ListeJoinDetailView, CreateShareRequestView,
    ShareRequestListView, AcceptShareRequestView, RefuseShareRequestView, ListeMembresView, ListeDemandesView)
from .views.produits import ProduitViewSet
from .views.logout import LogoutView
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'listes', ListeViewSet, basename='liste')
router.register(r'produits', ProduitViewSet, basename='produit')

urlpatterns = router.urls


urlpatterns += [
    path('listes/join/<uuid:share_token>/', ListeJoinDetailView.as_view(), name='liste-join'),
    path('listes/join/<uuid:share_token>/demande/', CreateShareRequestView.as_view(), name='demande-acces'),
    path('demandes/', ShareRequestListView.as_view(), name='demandes-list'),
    path('demandes/<int:pk>/accept/', AcceptShareRequestView.as_view(), name='demande-accepter'),
    path('demandes/<int:pk>/refuse/', RefuseShareRequestView.as_view(), name='demande-refuser'),
    path('listes/<int:pk>/followers/', ListeMembresView.as_view(), name='liste-membres'),
    path('listes/<int:pk>/share-requests/', ListeDemandesView.as_view(), name='liste-demandes'),
    path('logout/', LogoutView.as_view(), name='logout'),
]