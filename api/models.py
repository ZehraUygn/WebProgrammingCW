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
    
class Product(models.Model):
    """
    The model of the application represents a team with different details:
        - title
        - description
        - starting_price
        - picture of product
        - finish_date
        - highest bider - foreign key to user - helps to get user that is the highest bider
        - active - presents whether the product is currently listed or not
    """

    # Details of a product -- The item id is the PK auto-generated by Django
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    starting_price = models.PositiveSmallIntegerField()
    # picture = models.ImageField(upload_to="images", blank=True, default='../media/images/download.jpeg')

    # picture = models.ImageField(upload_to="images", blank=True, default='../media/images/download.png')
    picture = models.ImageField(upload_to="images", blank=True, default='../media/images/download.png')

    finish_date = models.DateField()
    active = models.BooleanField(default=True)
    bid_on = models.BooleanField(default=False)
    

    # foreign key to user - the highest bider
    highest_bidder = models.ForeignKey(
        to=User, blank=True, null=True, related_name="bid_on", on_delete=models.CASCADE
    )

    # foreign key to the owner of the product
    owner = models.ForeignKey(
        to=User, blank=True, null=True, related_name="owns", on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title

    def to_dict(self):
        """
        Transform the details of an item to a dictionary
        """
        return {
            "id": self.id,
            "active": self.active,
            "title": self.title,
            "description": self.description,
            "picture": self.picture.url if self.picture else None,
            "owner": self.owner.username,
            "starting_price": self.starting_price,
            "highest_bidder": self.highest_bidder.username,
            "finish_date": self.finish_date,
            "bid_on":self.bid_on
        }


class MessageResponse(models.Model):
    """
    Model that represents a reply from the owner to a message
    It contains a text field containing the reply
    """

    text = models.CharField(max_length=4096)

    def __str__(self):
        return self.text

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
        }


class Message(models.Model):
    """
    A user can send a message to the owner of the product
    This model contains: - sender - user that sends the message
                         - text of the message
                         - time - time the message was sent
    """

    sender = models.ForeignKey(to=User, related_name="sent", on_delete=models.CASCADE)
    text = models.CharField(max_length=4096)
    time = models.DateTimeField(default=timezone.now)  # Use timezone.now instead of datetime.now()

    # A product has many messages
    product = models.ForeignKey(
        to=Product,
        blank=True,
        null=True,
        related_name="about",
        on_delete=models.CASCADE,
    )

    # Each message can have only one reply
    message_response = models.ForeignKey(
        to=MessageResponse,
        default=1,
        blank=True,
        null=True,
        related_name="response",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"From {self.text} "

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender.username,
            "text": self.text,
            "product": self.product.id,
            "response_id": self.message_response.id,
            "time": self.time.strftime("%Y-%d-%mT%H:%M"),
        }
