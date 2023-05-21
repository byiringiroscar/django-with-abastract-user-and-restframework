from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None, is_admin=False, is_staff=False, is_active=True):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone_number:
            raise ValueError('Users must have an phone address')
        if not name:
            raise ValueError('Users must have name')

        user = self.model(
            phone_number=phone_number,
            name=name
        )
        user.set_password(password)
        # user.admin = is_admin
        # user.staff = is_staff
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone_number, name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(

            phone_number,
            name,
            password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone_number,
            name,
            password=password,

        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    # def create_superuser(self, phone_number, name, password=None, **extra_fields):
    #     if not phone_number:
    #         raise ValueError("User must have an phone_number")
    #     if not password:
    #         raise ValueError("User must have a password")
    #     if not name:
    #         raise ValueError("User must have a name")
    #
    #     user = self.model(
    #         phone_number=self.phone_number,
    #     )
    #     user.name = name
    #     user.set_password(password)
    #     user.admin = True
    #     user.staff = True
    #     user.active = True
    #     user.save(using=self._db)
    #     return user


class User(AbstractUser):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    username = None

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.phone_number

    def get_short_name(self):
        return self.phone_number

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    objects = UserManager()
