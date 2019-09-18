from django.db import models

# Create your models here.

"""
    Model to help store user data to the db
    user data eg:
        FirstName
        lastName
        nickname or username
        email
        password
        account_creation_date
    This is basic user data on registration
"""

class UserAuthentication(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    account_created_at = models.DateTimeField(auto_now=True)

    # Return user email 
    def __dict__(self):
        return {"email": self.email}
