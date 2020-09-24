from datetime import datetime

from django.db import models


# 覆盖默认django自带的用户表
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女"),
        ("unknown", u"不详")
    )


# class BaseModel(models.Model):
#     update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
#
#     class Meta:
#         abstract = True


class UserProfile(AbstractUser):
    """
    用户信息
    """
    nick_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="昵称")
    user_sn = models.CharField(max_length=50, verbose_name="用户ID", primary_key=True)
    user_avatar = models.ImageField(upload_to="avatar/%Y/%m", default="avatar/default.png", null=True, blank=True,
                                    verbose_name="用户头像")
    user_grade = models.CharField(max_length=5, null=True, blank=True, verbose_name="用户等级")
    user_birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    user_gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default="unknown", verbose_name="性别")
    user_mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    user_email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="注册时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = 'users'

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
