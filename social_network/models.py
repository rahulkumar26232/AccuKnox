from django.contrib.auth.models import AbstractUser
from django.db import models

from social_network.exceptions import SelfRequestException


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.pk)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class FriendRequest(models.Model):
    class StatusChoice(models.TextChoices):
        pending = 'pending', 'Pending'
        accept = 'accept', 'Accept'
        reject = 'reject', 'Reject'

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.pending)

    def clean(self):
        if self.from_user == self.to_user:
            raise SelfRequestException("Cannot send friend request to yourself.")

        super().clean()

    class Meta:
        unique_together = ['from_user', 'to_user']
