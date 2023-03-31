from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
class User(AbstractUser):
    email = models.EmailField()


# 引数にblank=Falseを入れる必要はない。
# デフォルトでblank=Falseとなるため。

# class FriendShip(models.Model):
