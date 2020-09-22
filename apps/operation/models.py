from django.db import models

# Create your models here.

from datetime import datetime

from apps.caricature.models import Caricature

from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()



class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.CASCADE)
    cartoon_name = models.ForeignKey(Caricature, related_name='fav_cartoon', verbose_name="漫画", help_text="漫画编号", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "cartoon_name")
        db_table = 'users_fav'

    def __str__(self):
        return self.user


class UserLeavingMessage(models.Model):
    """
    用户评论
    """
    user = models.ForeignKey(User, verbose_name="评论的用户", on_delete=models.CASCADE)
    cartoon = models.ForeignKey(Caricature, verbose_name="评论的漫画", on_delete=models.CASCADE)
    message = models.TextField(default="", verbose_name="评论内容", help_text="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message