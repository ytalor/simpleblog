from django.db import models


class Comment(models.Model):
    title = models.TextField()
    body = models.TextField()
    created_by = models.TextField()

    def __str__(self):
        return self.body
