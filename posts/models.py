from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    text = models.TextField()
    publication_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.text[:50]
