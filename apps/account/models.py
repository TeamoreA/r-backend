# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import BaseUserManager
# from helpers import fancy_id_generator

# class UserManager(BaseUserManager):
#     def create_user(
#         self, username, email, password=None, is_staff=False, **extra_fields
#     ):
#         """Create a user instance with the given email and password."""
#         if username is None:
#             raise TypeError("Users must have a username.")

#         # Google OAuth2 backend send unnecessary username field
#         extra_fields.pop("username", None)

#         if email is None:
#             raise TypeError("Users must have an email address.")

#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)

#         if password:
#             user.set_password(password)

#         user.save()

#         return user

# class User(AbstractBaseUser):
#     """new user model that inherits the abstract user"""
#     id = models.CharField(
#         db_index=True,
#         max_length=256,
#         default=fancy_id_generator,
#         primary_key=True,
#         editable=False,
#     )
#     username = models.CharField(db_index=True, max_length=255, unique=True)
#     email = models.EmailField(unique=True)

#     objects = UserManager()
#     def __str__(self):
#         """returns the string representation of User object"""
#         return self.username

#     @staticmethod
#     def get_user(username):
#         """returns a user when suplied a username"""
#         try:
#             user = User.objects.get(username=username)
#             return user

#         except Exception:
#             return False
    
