from datetime import *
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Our User models is a sub-class of Django's AbstractUser
    So we can make use of Django's authentication system
    """

    username = models.CharField(max_length=50, unique=True)

    # 1-1 relationship with a profile page - each user must have a profile page
    profile = models.OneToOneField(
        to="Profile", blank=True, null=True, on_delete=models.CASCADE
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    # dictionary transformation
    def to_dict(self):
        return {
            "username": self.username,
            "profile": self.profile.to_dict(),
            "messages": [message.to_dict() for message in self.messages],
        }

    @property
    def messages(self):
        """
        Messages sent and received by this user
        -> Sorted by time received
        """
        return (self.sent.all() | self.received.all()).order_by("-time")


class Profile(models.Model):
    """
    Profile class represents the profile details of the user
    Required fields: - email
                     - date of birth
                     - profile page
    """

    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField(null=True)
    # profile_picture = models.ImageField(upload_to="images", blank=True)

    profile_picture = models.ImageField(upload_to="images", blank=True, default='../media/images/images.png')
    # the foreign key is present because each user has a profile
    user_acc = models.ForeignKey(
        to=User, blank=True, null=True, related_name="of", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user_acc.username

    # dictionary transformation
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "date_of_birth": self.date_of_birth,
            "profile_picture": self.profile_picture.url
            if self.profile_picture
            else None,
        }