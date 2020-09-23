from django.db import models

# Create your models here.

from datetime import datetime

from apps.users.models import BaseModel
from apps.caricature.models import Caricature

from django.contrib.auth import get_user_model

# Create your models here.

UserProfile = get_user_model()


class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    cartoon_name = models.CharField(max_length=50, verbose_name=u"漫画")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CartoonComment(BaseModel):
    """
    用户评论/漫画评论内容
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    cartoon = models.ForeignKey(Caricature, on_delete=models.CASCADE, ValueError="漫画")
    comment = models.CharField(max_length=200, verbose_name="评论内容")

    class Meta:
        verbose_name = "漫画评论"
        verbose_name_plural = verbose_name
        db_table = "cartoon-comment"


class UserFav(BaseModel):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    cartoon_sn = models.CharField(max_length=30, verbose_name="漫画编号")
    cartoon_type = models.CharField(max_length=10, choices=(("serial", "连载中"), ("end", "已完结")), default="serial",
                                    verbose_name="漫画类型")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "cartoon_sn")
        db_table = 'users_fav'

    def __str__(self):
        return self.user


class UserMessage(BaseModel):
    """
    用户消息
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读消息")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name
        db_table = "user-message"

    def __str__(self):
        return self.user


class UserCartoon(BaseModel):
    """
    用户浏览漫画
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    cartoon = models.ForeignKey(Caricature, on_delete=models.CASCADE, ValueError="漫画")

    class Meta:
        verbose_name = "用户浏览漫画"
        verbose_name_plural = verbose_name
        db_table = "user-cartoon"

