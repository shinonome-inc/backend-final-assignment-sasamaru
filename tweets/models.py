from django.conf import settings
from django.db import models


class Tweet(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # tweetモデルがuserモデルを参照するため。
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # strは管理画面特有のもの。データを表示させたい。
    def __str__(self):
        return self.content
