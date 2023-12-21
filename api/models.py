from datetime import *
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    profile = models.OneToOneField(
        to="Profile", 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
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
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField(null=True)
    # profile_picture = models.ImageField(upload_to="images", blank=True)
    profile_picture = models.ImageField(upload_to="images", blank=True, default='../media/images/images.png')

    user_acc = models.ForeignKey(
        to=User, 
        blank=True, 
        null=True, 
        related_name="of", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user_acc.username

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "date_of_birth": self.date_of_birth,
            "profile_picture": self.profile_picture.url
            if self.profile_picture
            else None,
        }
    
    
class Category(models.Model):
    """
        The attribute of a category:
        - name
    """

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    
    
class Article(models.Model):
    """
    The attribute of an article:
        - title
        - content
        - category
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        null=False,  # Ensures that each article must have a category
        default=None 
    )

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category.to_dict() if self.category else None,
            "content": self.content,
        }

# class Comment(models.Model):
#     """
#     The attribute of a comment:
#         - comment
#         - article
#         - username
#     """

