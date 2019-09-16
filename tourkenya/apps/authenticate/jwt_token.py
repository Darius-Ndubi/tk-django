import jwt, os

import datetime

"""
    Class to create user token to be used as access token upon login
    It has a method that when creating the token, uses the payload as the email,
    sets time for token creation to the current epoch time. 
    sets the token to be not be valid 5 minutes before creation.
    sets the token expiry time to 2 hours.
"""


class UserAuthToken:

    def generate_access_token(user):
        pay_load = {"email": user.get('email'),
                    "iat": datetime.datetime.utcnow(),
                    "nbf": datetime.datetime.utcnow() + datetime.timedelta(
                        minutes=-5),
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(
                        minutes=120)
                    }
        # Create token to be used and encode it with applications' key
        jwt_token = {"token": jwt.encode(pay_load, os.getenv("SECRET_KEY"))}

        # Return user token created
        return (jwt_token)
