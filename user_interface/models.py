from django.db import models
from django.contrib.auth.models import AbstractUser
from categories.models import Category

class User (AbstractUser):
    is_blocked=models.BooleanField(default=False)
    email= models.EmailField(unique=True)
    subscribed_categories= models.ManyToManyField(Category, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @classmethod
    def get_object_or_none(cls, **kwargs):
        try:
            return User.objects.get(**kwargs)

        except User.DoesNotExist:
            return None

