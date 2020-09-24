from django.db import models

# Create your models here.

from datetime import datetime

from caricature.models import Cartoon

from django.contrib.auth import get_user_model


UserProfile = get_user_model()


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    cartoon_name = models.CharField(max_length=50, verbose_name=u"漫画")
    ask_time = models.DateTimeField(default=datetime.now, verbose_name="回答时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name
        db_table = "user_ask"


class CartoonComment(models.Model):
    """
    用户评论/漫画评论内容
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE, verbose_name="漫画")
    comment = models.CharField(max_length=200, verbose_name="评论内容")
    comment_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

    class Meta:
        verbose_name = "漫画评论"
        verbose_name_plural = verbose_name
        db_table = "cartoon_comment"


class UserFavorite(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    cartoon_sn = models.CharField(max_length=30, verbose_name="漫画编号")
    cartoon_type = models.CharField(max_length=10, choices=(("serial", "连载中"), ("end", "已完结")), default="serial",
                                    verbose_name="漫画类型")
    fav_time = models.DateTimeField(default=datetime.now, verbose_name="收藏时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "cartoon_sn")
        db_table = 'users_favorite'

    def __str__(self):
        return self.user


class UserMessage(models.Model):
    """
    用户消息
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读消息")
    message_time = models.DateTimeField(default=datetime.now, verbose_name="消息时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name
        db_table = "user_message"

    def __str__(self):
        return self.user


class UserCartoon(models.Model):
    """
    用户浏览漫画
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE, verbose_name="漫画")
    look_time = models.DateTimeField(default=datetime.now, verbose_name="浏览时间")

    class Meta:
        verbose_name = "用户浏览漫画"
        verbose_name_plural = verbose_name
        db_table = "user_cartoon"

