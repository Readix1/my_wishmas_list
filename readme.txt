

TODO:

Une page profil
Une page mes listes (copie de liste, suppression)
Une page pour les listes que je suis
Une page voir ma liste (possibilité d'ajouter ou supprimer des produits)
Une page édition de liste avec demande de partage (notif ?)


curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{"username": "", "password": ""}'

curl -X POST http://127.0.0.1:8000/api/listes/ -H "Authorization: Token 41aff3bee92511db4eacce6a740b4dc286114ad8" -H "Content-Type: application/json" -d '{"name": "Liste de Noel", "is_shared": false}'

curl -X PUT http://127.0.0.1:8000/api/listes/3/ -H "Authorization: Token 41aff3bee92511db4eacce6a740b4dc286114ad8" -H "Content-Type: application/json" -d '{"name": "Liste de Nowel", "is_shared": true}'

curl -X GET http://127.0.0.1:8000/api/listes/2/ -H "Authorization: Token 41aff3bee92511db4eacce6a740b4dc286114ad8" -H "Content-Type: application/json"


curl -X GET http://127.0.0.1:8000/api/listes/ -H "Authorization: Token 41aff3bee92511db4eacce6a740b4dc286114ad8" -H "Content-Type: application/json"

curl -X DELETE http://127.0.0.1:8000/api/listes/2/ -H "Authorization: Token 41aff3bee92511db4eacce6a740b4dc286114ad8" -H "Content-Type: application/json"

curl -X GET http://127.0.0.1:8000/api/listes/join/2ae861ca-1e20-43f3-8b76-ff615ad24b9a/ -H "Authorization: Token 953fdea292582301fff0245aa2ca229bbd9e26fe" -H "Content-Type: application/json"

curl -X GET http://127.0.0.1:8000/api/demandes/ -H "Authorization: Token 953fdea292582301fff0245aa2ca229bbd9e26fe" -H "Content-Type: application/json"


Méthode | URL | Action
GET | /api/listes/ | Lister mes listes
POST | /api/listes/ | Créer une liste
GET | /api/listes/<id>/ | Détail d’une liste
PUT | /api/listes/<id>/ | Modifier une liste
PATCH | /api/listes/<id>/ | Modifier partiellement
DELETE | /api/listes/<id>/ | Supprimer une liste

Méthode | Endpoint | Action
GET | /api/listes/join/<token>/ | Voir les infos de la liste
POST | /api/listes/join/<token>/ | Créer une demande d’accès
GET | /api/demandes/ | Voir toutes les demandes reçues (propriétaire)
POST | /api/demandes/<id>/accept/ | Accepter
POST | /api/demandes/<id>/refuse/ | Refuser