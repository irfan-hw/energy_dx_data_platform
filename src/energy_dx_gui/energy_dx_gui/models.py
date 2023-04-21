from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.apps import apps

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Houjin(models.Model):
    id = models.AutoField(primary_key=True)
    houjin_name = models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_houjin'

class Shisetsu(models.Model):
    id = models.AutoField(primary_key=True)
    shisetsu_name = models.CharField(max_length=100)
    houjin = models.ForeignKey(Houjin, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 't_shisetsu'

