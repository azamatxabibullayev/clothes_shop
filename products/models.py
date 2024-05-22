from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CategoryProducts(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category_products'

    def __str__(self):
        return self.name


class Clothes(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True,
                              default='default_images/watch_image.png')
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clothes'

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    clothe = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"Review by {self.user} for {self.clothe}"


class Order(models.Model):
    user = models.CharField(max_length=100)
    number = models.IntegerField()

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.number
