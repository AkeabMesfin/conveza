from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set email to None if empty to avoid UNIQUE constraint errors
        if self.email == "":
            self.email = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class SuperUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Superuser'
        verbose_name_plural = 'Admins'

class RegularUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Regular User'
        verbose_name_plural = 'Users'


