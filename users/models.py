from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models as m


# Create your models here.

class User(AbstractUser):  # is_superuser = admin
    avatar = m.ImageField("avatar", upload_to='profile_pics/', default='{% static "img/user_icon.png" %}', blank=True,
                          null=True)
    # REQUIRED_FIELDS = []


class EmailCodes(m.Model):
    code = m.IntegerField("Code", validators=[MaxValueValidator(6), MinValueValidator(1)])
