from django.db import models

# Create your models here.
# class Recipe(models.Model):
#     """
#     A model to create and manage recipes
#     """

#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, related_name="recipe_owner", on_delete=models.CASCADE
#     )
#     title = models.CharField(max_length=300, null=False, blank=False)
#     description = models.CharField(max_length=500, default="Pas de description")
#     instructions = models.TextField(max_length=10000, default="<ol> <li>Ajouter des instructions</li> </ol>")
#     ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantite')
#     accompagnementStandard = models.CharField(max_length=300, default="")
#     image = ResizedImageField(
#         size=[400, None],
#         quality=75,
#         upload_to="recipes/",
#         force_format="WEBP",
#         default="recipes/default_recipe.png",
#         blank=False,
#         null=False,
#     )
#     image_alt = models.CharField(max_length=100, default="Recipe image")
#     meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="all")

#     calories = models.IntegerField(default=0)
#     posted_date = models.DateTimeField(auto_now=True)
