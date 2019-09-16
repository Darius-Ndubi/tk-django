from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models


class UserManager(BaseUserManager):

    """
        Class method to create a new user to the appliction. It handles user registration
        It takes in user:
            firstName
            lastName
            username
            email
            password
    """

    def create_user(self, firstName,
                    lastName, username, email, password=None, is_active=True):

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        if firstName is None:
            raise TypeError('Kindly enter your Last name.')

        if lastName is None:
            raise TypeError('Kindly enter your Last name.')

        """Create and return a new_user with an email, firstName, lastName username and password."""
        user = self.model(firstName=firstName, lastName=lastName,
                          username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = is_active
        user.save()

        return user


"""
    Class to specify the user fields to be added to the database
"""


class User(AbstractBaseUser):
    firstName = models.CharField("User's first name", max_length=50, null=False)
    lastName = models.CharField("User's last name", max_length=50, null=False)
    username = models.CharField("User's username", max_length=50, unique=True)
    pictureUlr = models.CharField("User's picture", max_length=254, default="https://randomuser.me/api/portraits/women/60.jpg")
    email = models.EmailField("User's email", max_length=254, unique=True)
    password = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    # Method to return user info due to query to db
    def dict(self):
        return ({"email": self.email, "username": self.username})
