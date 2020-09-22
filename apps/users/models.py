from django.db import models

# Create your models here.


from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from apps.caricature.models import Caricature

# User = get_user_model()


# Create your models here.

class UserProfile(models.Model):
    """
    用户信息
    """
    user_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    user_sn = models.CharField(max_length=50, verbose_name="用户ID", primary_key=True)
    user_birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    user_gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female", verbose_name="性别")
    user_mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    user_email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = 'users'

    def __str__(self):
        return self.user_name


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
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
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                       help_text=u"留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)")
    subject = models.CharField(max_length=100, default="", verbose_name="主题")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject