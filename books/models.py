from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        editable=False,
        unique=True
    )
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    class Meta:
        permissions = [
            ('special_status', 'Can read all books')
        ]

    def get_authors(self):
        return "\n".join([a.name for a in self.author.all()])

    def get_reviews(self):
        return "\n".join([f'{r.author}: {r.review}' for r in self.reviews.all()])

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.review
