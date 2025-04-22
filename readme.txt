

TODO:

calendrier:
pour le mois contraction des utilisateurs dans un bandeau déroulant
faire un affichage semaine ou on voit tous les mangeurs avec les accompagnements

utilisateurs : ajouter des mangeurs pour faire une famille
pouvoir ajouter des utilisateurs pour partager la famille


curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "", "password": ""}'

curl -X POST http://127.0.0.1:8000/api/listes/ -H "Authorization: Token 41aff3bee92511db4eacce6a740b4dc286114ad8" -H "Content-Type: application/json" -d '{"name": "Liste de Noël", "is_shared": false}'

Méthode | URL | Action
GET | /api/listes/ | Lister mes listes
POST | /api/listes/ | Créer une liste
GET | /api/listes/<id>/ | Détail d’une liste
PUT | /api/listes/<id>/ | Modifier une liste
PATCH | /api/listes/<id>/ | Modifier partiellement
DELETE | /api/listes/<id>/ | Supprimer une liste