from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"Author: {self.name}"


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateField()
    author = models.ForeignKey(
        Author,
        related_name="articles",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Article: {self.title}"
