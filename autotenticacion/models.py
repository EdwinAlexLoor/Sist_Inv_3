from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core import validators
from django.core.validators import RegexValidator, validate_email
from django.urls import reverse
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(('username'), max_length=200, unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[a-z0-9_-]*$',
            message='Usernames can only contain letters, numbers, underscores, and dashes.'
        )
    ])

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[validators.validate_email]
    )

    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def __str__(self):
        return '{}{}{}'.format(self.username, " ", self.email)

    def get_absolute_url(self):
        return reverse('modificar_usuario', kwargs={'pk': self.pk})

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
        # Simplest possible answer: All admins are staff
        return self.is_admin

class Persona(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

class UsuarioPersona(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Rol(models.Model):
    nombre = models.CharField(max_length=90)

    def __str__(self):
        return '{}'.format(self.nombre)



class RolUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return '{}{}{}'.format(self.usuario, " ", self.rol)