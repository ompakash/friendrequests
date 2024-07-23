from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.email)
    

class FriendRequest(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_friend_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_friend_requests', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.receiver)
    