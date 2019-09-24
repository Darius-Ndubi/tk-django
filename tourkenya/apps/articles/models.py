"""
    Models file to create db columns
"""
from django.db import models

# Create your models here.
from tourkenya.apps.authenticate.models import User

"""
    Class to define the db columns on an article.
"""


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    draft = models.BooleanField(default=True)
    posted = models.BooleanField(default=False)
